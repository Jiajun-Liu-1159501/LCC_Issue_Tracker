from collections.abc import MutableMapping
from typing import TypeVar, Generic, Optional
import threading

K = TypeVar("K")
V = TypeVar("V")

class ConcurrentDict(MutableMapping, Generic[K, V]):
    
    def __init__(self) -> None:
        self._dict: dict[K, V] = {}
        self._lock = threading.RLock()

    def __setitem__(self, key: K, value: V) -> None:
        with self._lock:
            self._dict[key] = value

    def __getitem__(self, key: K) -> V:
        with self._lock:
            return self._dict[key]

    def __delitem__(self, key: K) -> None:
        with self._lock:
            del self._dict[key]

    def __iter__(self):
        with self._lock:
            return iter(self._dict.copy())

    def __len__(self) -> int:
        with self._lock:
            return len(self._dict)

    def get(self, key: K, default: Optional[V] = None) -> Optional[V]:
        with self._lock:
            return self._dict.get(key, default)

