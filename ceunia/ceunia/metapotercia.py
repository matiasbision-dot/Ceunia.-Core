
def update_metapotercia(meta, scores):
    avg = sum(scores) / len(scores)

    if avg > 0.6:
        meta["alpha"] = min(0.9, meta["alpha"] + 0.05)
    else:
        meta["alpha"] = max(0.1, meta["alpha"] - 0.05)

    return meta
