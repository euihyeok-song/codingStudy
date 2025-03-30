def solution(data, ext, val_ext, sort_by):
    idx = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    ext_idx = idx[ext]
    sort_idx= idx[sort_by]
    filtered_data = [item for item in data if item[ext_idx] < val_ext]
    return sorted(filtered_data, key=lambda x: x[sort_idx])
