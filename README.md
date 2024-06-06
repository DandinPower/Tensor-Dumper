# Tensor-Dumper
- a Tensor dumper for PyTorch, supporting different data types and compression.

## Usage

1. install it
    ```bash
    pip install .
    ```

2. Use it in your code
    ```python
    import torch
    from dumper import Dumper

    # Save a tensor to a file
    tensor = torch.tensor([[1, 2], [3, 4]])
    Dumper.save_tensor("my_tensor.npz", tensor)

    # Load a tensor from a file
    loaded_tensor = Dumper.load_tensor("my_tensor.npz")
    ```

## Features

- Save PyTorch tensors to disk in `.npz` format.
- Load PyTorch tensors from `.npz` files.
- Supports both compressed and uncompressed saving.
- Supports various data types including `float32`, `float16`, `int`, and `bool`.

## API

### Save a tensor to a file

`Dumper.save_tensor(filename: str, tensor: torch.Tensor, is_compressed: bool = True) -> None`

- **Args:**
    - `filename` (str): The name of the file to save the tensor to.
    - `tensor` (torch.Tensor): The tensor to be saved.
    - `is_compressed` (bool, optional): Whether to compress the saved file using `np.savez_compressed`. 
        Defaults to `True`.
- **Returns:**
    - `None`

### Load a tensor from a file as a NumPy array

`Dumper.load_tensor_in_numpy(filename) -> np.ndarray`

- **Args:**
    - `filename` (str): The path to the file containing the tensor.
- **Returns:**
    - `np.ndarray`: The loaded tensor as a NumPy array.

### Load a tensor from a file as a PyTorch tensor

`Dumper.load_tensor(filename) -> torch.Tensor`

- **Args:**
    - `filename` (str): The path to the file containing the tensor.
- **Returns:**
    - `torch.Tensor`: The loaded tensor.

## Testing

Run the following command in the root directory to run the tests:

```bash
python tests/test_dumper_class.py
```