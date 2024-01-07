'''OpenGL extension ARB.create_context_profile

This module customises the behaviour of the 
OpenGL.raw.WGL.ARB.create_context_profile to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/create_context_profile.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.WGL import _types, _glgets
from OpenGL.raw.WGL.ARB.create_context_profile import *
from OpenGL.raw.WGL.ARB.create_context_profile import _EXTENSION_NAME

def glInitCreateContextProfileARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION