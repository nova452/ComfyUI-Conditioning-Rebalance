from .nodes import ConditioningKrea2Rebalance

NODE_CLASS_MAPPINGS = {
    "ConditioningKrea2Rebalance": ConditioningKrea2Rebalance,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ConditioningKrea2Rebalance": "Conditioning Krea2 Rebalance",
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
