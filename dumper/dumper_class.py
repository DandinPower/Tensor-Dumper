import torch
import numpy as np
import os
from .utils import ensure_dir_exists_by_filename

class Dumper:
    """A class for dumping tensors to disk."""
    @staticmethod
    def save_tensor(filename: str, tensor: torch.Tensor, is_compressed: bool = True) -> None:
        """
        Save a tensor to a file.

        Args:
            filename (str): The name of the file to save the tensor to.
            tensor (torch.Tensor): The tensor to be saved.
            is_compressed (bool, optional): Whether to compress the saved file using np.savez_compressed. 
                Defaults to True.

        Returns:
            None
        """
        ensure_dir_exists_by_filename(filename)
        array = tensor.detach().numpy()
        if is_compressed:
            np.savez_compressed(filename, array=array)
        else:
            np.savez(filename, array=array)

    @staticmethod
    def load_tensor_in_numpy(filename) -> np.ndarray:
        """
        Load a tensor from a file.

        Args:
            filename (str): The path to the file containing the tensor.

        Returns:
            np.ndarray: The loaded tensor.
        """
        assert os.path.exists(filename), f"File {filename} does not exist."
        with np.load(filename, allow_pickle=True) as data:
            array = data['array']
        return array

    @staticmethod
    def load_tensor(filename) -> torch.Tensor:
        """
        Load a tensor from a file.

        Args:
            filename (str): The path to the file containing the tensor.

        Returns:
            torch.Tensor: The loaded tensor.
        """
        assert os.path.exists(filename), f"File {filename} does not exist."
        array = Dumper.load_tensor_in_numpy(filename)
        tensor = torch.from_numpy(array)
        return tensor