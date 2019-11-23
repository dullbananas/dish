# Dish
Dish is a new, modern Unix shell implemented in pure Python with Flask-like configuration and extensibility. It works by having a Python script called "dish.py" somewhere in `PATH`. This script looks a bit like a single-file Flask application. Here is a minimal example:

```python3
#!/usr/bin/env python3

from dish import Dish
dish = Dish()

if __name__ == '__main__':
    dish.run()
```
