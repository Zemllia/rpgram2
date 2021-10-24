class Inventory:
    items = []

    def add_item(self, item):
        for cur_item in self.items:
            if cur_item.name == item.name:
                if not cur_item.max_stack > item.count + cur_item.count:
                    cur_item.count = item.count + cur_item.count
                    return True
        self.items.append(item)
        return True

    def delete_item_by_id(self, item_id):
        for item in self.items:
            if item.item_id == item_id:
                self.items.remove(item)

    def drop_from_inventory_by_place(self, place: int, count):
        cur_item = self.items[place]
        map_object = cur_item.instantiate_to_map_object()
        if count <= cur_item.items_count > 0:
            cur_item.items_count -= count
        if cur_item.items_count <= 0:
            self.items.pop(place)
        return map_object

    def get_inventory(self):
        final_inventory_string = ""
        counter = 1
        for item in self.items:
            final_inventory_string += str(counter) + ". " + item.name + " x" + item.items_count + "\n"
