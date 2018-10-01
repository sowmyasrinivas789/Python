def rec_set(self, my_dict, key_list, val):
    if len(key_list) <= 0:
        return
    elif len(key_list) == 1:
        my_dict[key_list.pop(0)] = val
    else:
        self.rec_set(my_dict[key_list.pop(0)], key_list, val)

data = {"copy_print_parameter/copy_print_paper_size/paper_size": "zero"}

def get_body(self, data):
    default_body = {"auto_adjust": True, "copy_print_parameter": {"copy_print_paper_size": {"paper_size": "auto"},
                                                                  "copy_density": "positive1"},
                    "copy_scan_parameter": {"copy_scan_paper_size": {"paper_size": "auto"}, "image_mode": "text",
                                            "copy_color_mode": "black", "drop_out_color": True,
                                            "drop_out_color_level": "-3"}, "auto_event": False}
    for each in data:
        if each in {"skip", "Expected result", "preconditions"}:
            continue
        key_list = each.split('/')
        self.rec_set(default_body, key_list, data[each])
    return default_body