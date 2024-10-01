# tests/helpers.py

from typing import Any, Set, Optional, List, Dict

class ExcalidrawComparator:
    """
    A simplified comparator class to compare two Excalidraw JSON objects,
    normalizing IDs and ignoring specified fields.
    """

    def __init__(self, ignore_fields: Optional[Set[str]] = None) -> None:
        """
        Initialize the comparator with a set of fields to ignore.

        :param ignore_fields: A set of field names to ignore during comparison.
        """
        if ignore_fields is None:
            ignore_fields = set()
        self.ignore_fields: Set[str] = ignore_fields
        self.differences: List[str] = []

    def compare(self, expected: Dict[str, Any], actual: Dict[str, Any]) -> bool:
        """
        Compare two Excalidraw JSON objects after normalizing IDs.

        :param expected: The reference JSON object.
        :param actual: The generated JSON object to compare.
        :return: True if the JSON objects are equal, False otherwise.
        """
        self.differences.clear()

        # Normalize both JSONs
        expected_normalized = self._normalize_excalidraw_json(expected)
        actual_normalized = self._normalize_excalidraw_json(actual)

        # Proceed with comparison
        result = self._compare_recursive(expected_normalized, actual_normalized)
        if not result:
            print("Differences found:")
            for diff in self.differences:
                print(diff)
        return result

    def _normalize_excalidraw_json(self, excalidraw_json: Dict[str, Any]) -> Dict[str, Any]:
        """
        Normalize the IDs in the entire Excalidraw JSON.

        :param excalidraw_json: The Excalidraw JSON dictionary.
        :return: A new Excalidraw JSON dictionary with normalized IDs.
        """
        excalidraw_json = excalidraw_json.copy()
        elements = excalidraw_json.get('elements', [])
        normalized_elements = self._normalize_ids(elements)
        excalidraw_json['elements'] = normalized_elements

        # No need to normalize 'files' in this simplified version
        return excalidraw_json

    def _normalize_ids(self, elements: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Normalize the IDs of elements by replacing them with placeholder IDs based on their index.

        :param elements: List of element dictionaries.
        :return: The list of elements with normalized IDs.
        """
        id_mapping: Dict[str, str] = {}

        # First, build the ID mapping for all elements
        for idx, element in enumerate(elements):
            original_id = element['id']
            placeholder_id = f'element_{idx}'
            id_mapping[original_id] = placeholder_id

        # Now, replace IDs in each element
        normalized_elements: List[Dict[str, Any]] = []
        for element in elements:
            normalized_element = self._replace_ids_in_element(element, id_mapping)
            normalized_elements.append(normalized_element)

        return normalized_elements
        
    def _replace_ids_in_element(self, element: Dict[str, Any], id_mapping: Dict[str, str]) -> Dict[str, Any]:
        """
        Replace IDs in the element and its references using the provided ID mapping.

        :param element: The element dictionary.
        :param id_mapping: Mapping from original IDs to placeholder IDs.
        :return: The element dictionary with IDs replaced.
        """
        element = element.copy()
        element['id'] = id_mapping.get(element['id'], element['id'])

        # Replace IDs in boundElements
        if 'boundElements' in element and element['boundElements']:
            new_bound_elements = []
            for bound in element['boundElements']:
                new_bound = bound.copy()
                new_bound['id'] = id_mapping.get(bound['id'], bound['id'])
                new_bound_elements.append(new_bound)
            element['boundElements'] = new_bound_elements

        # Replace IDs in startBinding and endBinding
        for binding_key in ['startBinding', 'endBinding']:
            if binding_key in element and element[binding_key]:
                binding = element[binding_key].copy()
                binding['elementId'] = id_mapping.get(binding['elementId'], binding['elementId'])
                element[binding_key] = binding

        # Replace IDs in groupIds
        if 'groupIds' in element and element['groupIds']:
            element['groupIds'] = [id_mapping.get(gid, gid) for gid in element['groupIds']]

        return element

    def _compare_recursive(self, obj1: Any, obj2: Any, path: str = '') -> bool:
        """
        Internal method to recursively compare two JSON objects.

        :param obj1: First JSON object.
        :param obj2: Second JSON object.
        :param path: The JSON path to the current object being compared.
        :return: True if objects are equal (ignoring specified fields), False otherwise.
        """
        if type(obj1) != type(obj2):
            self.differences.append(f"Type mismatch at '{path}': {type(obj1).__name__} != {type(obj2).__name__}")
            return False

        if isinstance(obj1, dict):
            keys1 = set(obj1.keys()) - self.ignore_fields
            keys2 = set(obj2.keys()) - self.ignore_fields
            if keys1 != keys2:
                missing_in_obj1 = keys2 - keys1
                missing_in_obj2 = keys1 - keys2
                if missing_in_obj1:
                    self.differences.append(f"Keys missing in expected at '{path}': {missing_in_obj1}")
                if missing_in_obj2:
                    self.differences.append(f"Keys missing in actual at '{path}': {missing_in_obj2}")
                return False
            for key in keys1:
                new_path = f"{path}.{key}" if path else key
                if not self._compare_recursive(obj1[key], obj2[key], new_path):
                    return False
            return True
        elif isinstance(obj1, list):
            if len(obj1) != len(obj2):
                self.differences.append(f"List length mismatch at '{path}': {len(obj1)} != {len(obj2)}")
                return False
            for index, (item1, item2) in enumerate(zip(obj1, obj2)):
                new_path = f"{path}[{index}]"
                if not self._compare_recursive(item1, item2, new_path):
                    return False
            return True
        else:
            if obj1 != obj2:
                self.differences.append(f"Value mismatch at '{path}': {obj1} != {obj2}")
                return False
            return True
