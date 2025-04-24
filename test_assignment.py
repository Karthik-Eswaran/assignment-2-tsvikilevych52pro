import pytest
import assignment
import os

def test_read_file(tmp_path):
    # Create a temporary file
    file_path = tmp_path / "test_file.txt"
    file_path.write_text("Hello, World!")
    
    # Test the read_file function
    assert assignment.read_file(str(file_path)) == "Hello, World!"

def test_write_file(tmp_path):
    # Create a temporary file path
    file_path = tmp_path / "test_file.txt"
    
    # Test the write_file function
    assignment.write_file(str(file_path), "Hello, Python!")
    assert file_path.read_text() == "Hello, Python!"

def test_list_files_in_directory(tmp_path):
    # Create temporary files in a directory
    (tmp_path / "file1.txt").touch()
    (tmp_path / "file2.py").touch()
    (tmp_path / "file3.md").touch()
    
    # Test the list_files_in_directory function
    files = assignment.list_files_in_directory(str(tmp_path))
    assert sorted(files) == sorted(["file1.txt", "file2.py", "file3.md"])

def test_generate_numbers():
    # Test the generate_numbers function
    gen = assignment.generate_numbers(5)
    assert list(gen) == [0, 1, 2, 3, 4]

def test_use_function_from_module(tmp_path):
    # Create a temporary module file
    module_path = tmp_path / "temp_module.py"
    module_path.write_text("""
def sample_function(x, y):
    return x + y
""")
    
    # Add the temporary directory to the Python path
    import sys
    sys.path.append(str(tmp_path))
    
    # Test the use_function_from_module function
    result = assignment.use_function_from_module("temp_module", "sample_function", 3, 4)
    assert result == 7
    
    # Clean up the Python path
    sys.path.remove(str(tmp_path))
