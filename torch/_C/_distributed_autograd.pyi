import torch
from typing import Dict

# distributed/autograd/init.cpp
class DistAutogradContext:
    def _context_id(self) -> int: ...
def _init(default_node_id: int) -> None: ...
def _get_debug_info() -> Dict[str, str]: ...
def _new_context() -> DistAutogradContext: ...
def _release_context(context_id: int) -> None: ...
def get_gradients(context_id: int) -> Dict[torch.Tensor, torch.Tensor]: ...
def _is_valid_context(worker_id: int) -> bool: ...
