def charge_per_size(size: int) -> float:
    if size <= 500:
        return 5
    return 12.5


def charge_per_length(sec: int) -> float:
    THRESHOLD_LENGTH = 387  # 6 min 18 sec
    if sec <= THRESHOLD_LENGTH:
        return 12.5
    return 20


def total_pricing(size: float, sec: int) -> float:
    return charge_per_length(sec) + charge_per_size(size)


def json_total_pricing(size, sec):
    size_price = charge_per_size(size)
    length_price = charge_per_length(sec)
    total_price = size_price + length_price
    return {"size_wise_price": size_price, "length_wise_price": length_price, "total_price": total_price}
