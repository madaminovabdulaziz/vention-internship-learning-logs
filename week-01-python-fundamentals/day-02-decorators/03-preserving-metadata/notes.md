So, decorators have a hidden small problem


When we write a decorator, and assign it to some function, so our function is no longer original function, it will be wrapper function that timer built, so that's why, when we ask foo.__name__ or foo.__doc__ we are actually asking for wrapper.__name__, wrapper.__doc__


The original function is still inside the wrappers closure, but it's metadata (name, docstring, signature) is hidden. From outside world, our functions looks like some genereic wrapper not foo


Why this matters:

Debugging
Doc tools
Logging
Tests


What @wraps Actually Copies
Under the hood, @wraps(func) copies these attributes from func onto wrapper:

__name__ — the function's name
__doc__ — the docstring
__module__ — which module it came from
__qualname__ — fully qualified name
__dict__ — any custom attributes
__wrapped__ — a reference to the original function (so you can still reach it if you need)