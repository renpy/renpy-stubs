from _frozen_importlib import BuiltinImporter as BuiltinImporter
from typing import Sequence

type GLenum = int
type GLuint = int
type GLint = int
type GLbitfield = int
type GLsizei = int

type GLenum_ptr = int
type GLuint_ptr = int
type GLint_ptr = int
type GLbitfield_ptr = int
type GLsizei_ptr = int
type str_ptr = str
type float_ptr = float
type GLvoid_ptr = int
type GLvoid_ptr_ptr = int

class Buffer:
    def __buffer__(self, flags: int) -> memoryview: ...
    def __release_buffer__(self, buffer: GLuint) -> None: ...

class BytesBuffer(Buffer):
    def __init__(self, length: int) -> None: ...
    def get(self) -> bytes: ...
    def __init__(self, length: int) -> None: ...
    def get(self) -> bytes: ...

class BytesListBuffer(Buffer):
    def __init__(self, value: Sequence[bytes]) -> None: ...

class FloatBuffer(Buffer):
    def __init__(self, value: Sequence[float]) -> None: ...
    def __getitem__(self, key: int) -> float: ...
    def __init__(self, value: Sequence[float]) -> None: ...
    def __getitem__(self, key: int) -> float: ...

class IntBuffer(Buffer):
    def __init__(self, value: Sequence[int]) -> None: ...
    def __getitem__(self, key: int) -> int: ...
    def __init__(self, value: Sequence[int]) -> None: ...
    def __getitem__(self, key: int) -> int: ...

def glActiveTexture(texture: GLenum) -> None: ...
def glAttachShader(program: GLuint, shader: GLuint) -> None: ...
def glBeginQuery(target: GLenum, id: GLuint) -> None: ...
def glBeginTransformFeedback(primitiveMode: GLenum) -> None: ...
def glBindAttribLocation(program: GLuint, index: GLuint, name: str) -> None: ...
def glBindBuffer(target: GLenum, buffer: GLuint) -> None: ...
def glBindBufferBase(target: GLenum, index: GLuint, buffer: GLuint) -> None: ...
def glBindBufferRange(target: GLenum, index: GLuint, buffer: GLuint, offset: GLint, size: GLsizei) -> None: ...
def glBindFramebuffer(target: GLenum, framebuffer: GLuint) -> None: ...
def glBindRenderbuffer(target: GLenum, renderbuffer: GLuint) -> None: ...
def glBindTexture(target: GLenum, texture: GLuint) -> None: ...
def glBindVertexArray(array: GLuint) -> None: ...
def glBlendColor(red: float, green: float, blue: float, alpha: float) -> None: ...
def glBlendEquation(mode: GLenum) -> None: ...
def glBlendEquationSeparate(modeRGB: GLenum, modeAlpha: GLenum) -> None: ...
def glBlendFunc(sfactor: GLenum, dfactor: GLenum) -> None: ...
def glBlendFuncSeparate(sfactorRGB: GLenum, dfactorRGB: GLenum, sfactorAlpha: GLenum, dfactorAlpha: GLenum) -> None: ...
def glBlitFramebuffer(
    srcX0: GLint,
    srcY0: GLint,
    srcX1: GLint,
    srcY1: GLint,
    dstX0: GLint,
    dstY0: GLint,
    dstX1: GLint,
    dstY1: GLint,
    mask: GLbitfield,
    filter: GLenum,
) -> None: ...
def glBufferData(target: GLenum, size: GLsizei, data: GLvoid_ptr, usage: GLenum) -> None: ...
def glBufferSubData(target: GLenum, offset: GLint, size: GLsizei, data: GLvoid_ptr) -> None: ...
def glCheckFramebufferStatus(target: int) -> int: ...
def glClear(mask: GLbitfield) -> None: ...
def glClearBufferfi(buffer: GLuint, drawbuffer: GLint, depth: float, stencil: GLint) -> None: ...
def glClearBufferfv(buffer: GLuint, drawbuffer: GLint, value: list[float]) -> None: ...
def glClearBufferiv(buffer: GLuint, drawbuffer: GLint, value: list[GLint]) -> None: ...
def glClearBufferuiv(buffer: GLuint, drawbuffer: GLint, value: list[GLuint]) -> None: ...
def glClearColor(red: float, green: float, blue: float, alpha: float) -> None: ...
def glClearStencil(s: GLint) -> None: ...
def glColorMask(red: float, green: float, blue: float, alpha: float) -> None: ...
def glCompileShader(shader: GLuint) -> None: ...
def glCompressedTexImage2D(
    target: GLenum,
    level: GLint,
    internalformat: GLenum,
    width: GLsizei,
    height: GLsizei,
    border: GLint,
    imageSize: GLsizei,
    data: GLvoid_ptr,
) -> None: ...
def glCompressedTexImage3D(
    target: GLenum,
    level: GLint,
    internalformat: GLenum,
    width: GLsizei,
    height: GLsizei,
    depth: GLsizei,
    border: GLint,
    imageSize: GLsizei,
    data: GLvoid_ptr,
) -> None: ...
def glCompressedTexSubImage2D(
    target: GLenum,
    level: GLint,
    xoffset: GLint,
    yoffset: GLint,
    width: GLsizei,
    height: GLsizei,
    format: GLenum,
    imageSize: GLsizei,
    data: GLvoid_ptr,
) -> None: ...
def glCompressedTexSubImage3D(
    target: GLenum,
    level: GLint,
    xoffset: GLint,
    yoffset: GLint,
    zoffset: GLint,
    width: GLsizei,
    height: GLsizei,
    depth: GLsizei,
    format: GLenum,
    imageSize: GLsizei,
    data: GLvoid_ptr,
) -> None: ...
def glCopyTexImage2D(
    target: GLenum,
    level: GLint,
    internalformat: GLenum,
    x: GLint,
    y: GLint,
    width: GLsizei,
    height: GLsizei,
    border: GLint,
) -> None: ...
def glCopyTexSubImage2D(
    target: GLenum,
    level: GLint,
    xoffset: GLint,
    yoffset: GLint,
    x: GLint,
    y: GLint,
    width: GLsizei,
    height: GLsizei,
) -> None: ...
def glCopyTexSubImage3D(
    target: GLenum,
    level: GLint,
    xoffset: GLint,
    yoffset: GLint,
    zoffset: GLint,
    x: GLint,
    y: GLint,
    width: GLsizei,
    height: GLsizei,
) -> None: ...
def glCreateProgram() -> GLuint: ...
def glCreateShader(type: GLenum) -> GLuint: ...
def glCullFace(mode: GLenum) -> None: ...
def glDeleteBuffers(n: GLsizei, buffers: list[GLuint]) -> None: ...
def glDeleteFramebuffers(n: GLsizei, framebuffers: list[GLuint]) -> None: ...
def glDeleteProgram(program: GLuint) -> None: ...
def glDeleteQueries(n: GLsizei, ids: list[GLuint]) -> None: ...
def glDeleteRenderbuffers(n: GLsizei, renderbuffers: list[GLuint]) -> None: ...
def glDeleteShader(shader: GLuint) -> None: ...
def glDeleteTextures(n: GLsizei, textures: list[GLuint]) -> None: ...
def glDeleteVertexArrays(n: GLsizei, arrays: list[GLuint]) -> None: ...
def glDepthFunc(func: GLenum) -> None: ...
def glDepthMask(flag: bool) -> None: ...
def glDetachShader(program: GLuint, shader: GLuint) -> None: ...
def glDisable(cap: GLenum) -> None: ...
def glDisableVertexAttribArray(index: GLuint) -> None: ...
def glDrawArrays(mode: GLenum, first: GLint, count: GLsizei) -> None: ...
def glDrawBuffers(n: GLsizei, bufs: list[GLenum]) -> None: ...
def glDrawElements(mode: GLenum, count: GLsizei, type: GLenum, indices: GLvoid_ptr) -> None: ...
def glDrawRangeElements(
    mode: GLenum, start: GLuint, end: GLuint, count: GLsizei, type: GLenum, indices: GLvoid_ptr
) -> None: ...
def glEnable(cap: GLenum) -> None: ...
def glEnableVertexAttribArray(index: GLuint) -> None: ...
def glEndQuery(target: GLenum) -> None: ...
def glEndTransformFeedback() -> None: ...
def glFinish() -> None: ...
def glFlush() -> None: ...
def glFlushMappedBufferRange(target: GLenum, offset: GLint, length: GLsizei) -> None: ...
def glFramebufferRenderbuffer(
    target: GLenum, attachment: GLenum, renderbuffertarget: GLenum, renderbuffer: GLuint
) -> None: ...
def glFramebufferTexture2D(
    target: GLenum, attachment: GLenum, textarget: GLenum, texture: GLuint, level: GLint
) -> None: ...
def glFramebufferTextureLayer(
    target: GLenum, attachment: GLenum, texture: GLuint, level: GLint, layer: GLint
) -> None: ...
def glFrontFace(mode: GLenum) -> None: ...
def glGenBuffers(n: GLsizei, buffers: list[GLuint]) -> None: ...
def glGenFramebuffers(n: GLsizei, framebuffers: list[GLuint]) -> None: ...
def glGenQueries(n: GLsizei, ids: list[GLuint]) -> None: ...
def glGenRenderbuffers(n: GLsizei, renderbuffers: list[GLuint]) -> None: ...
def glGenTextures(n: GLsizei, textures: list[GLuint]) -> None: ...
def glGenVertexArrays(n: GLsizei, arrays: list[GLuint]) -> None: ...
def glGenerateMipmap(target: GLenum) -> None: ...
def glGetActiveAttrib(
    program: GLuint,
    index: GLuint,
    bufSize: GLsizei,
    length: GLsizei_ptr,
    size: GLint_ptr,
    type: GLenum_ptr,
    name: str_ptr,
) -> None: ...
def glGetActiveUniform(
    program: GLuint,
    index: GLuint,
    bufSize: GLsizei_ptr,
    length: GLsizei_ptr,
    size: GLint_ptr,
    type: GLenum_ptr,
    name: str_ptr,
) -> None: ...
def glGetAttachedShaders(program: GLuint, maxCount: GLsizei, count: GLsizei_ptr, shaders: list[GLuint]) -> None: ...
def glGetAttribLocation(program: GLuint, name: str) -> int: ...
def glGetBooleanv(pname: GLenum, data: GLvoid_ptr) -> None: ...
def glGetBufferParameteriv(target: GLenum, pname: GLenum, params: list[GLuint]) -> None: ...
def glGetBufferPointerv(target: GLenum, pname: GLenum, params: GLvoid_ptr_ptr) -> None: ...
def glGetError() -> int: ...
def glGetFloatv(pname: GLenum, data: GLvoid_ptr) -> None: ...
def glGetFragDataLocation(program: GLuint, name: str) -> int: ...
def glGetFramebufferAttachmentParameteriv(
    target: GLenum, attachment: GLenum, pname: GLenum, params: GLint_ptr
) -> None: ...
def glGetIntegeri_v(target: GLenum, index: GLuint, data: GLvoid_ptr) -> None: ...
def glGetIntegerv(pname: GLenum, data: GLvoid_ptr) -> None: ...
def glGetProgramInfoLog(program: GLuint, bufSize: GLsizei, length: GLsizei_ptr, infoLog: str_ptr) -> None: ...
def glGetProgramiv(program: GLuint, pname: GLenum, params: GLint_ptr) -> None: ...
def glGetQueryObjectuiv(id: GLuint, pname: GLenum, params: GLuint_ptr) -> None: ...
def glGetQueryiv(target: GLenum, pname: GLenum, params: GLint_ptr) -> None: ...
def glGetRenderbufferParameteriv(target: GLenum, pname: GLenum, params: list[GLint]) -> None: ...
def glGetShaderInfoLog(shader: GLuint, bufSize: GLsizei, length: GLsizei_ptr, infoLog: str_ptr) -> None: ...
def glGetShaderSource(shader: GLuint, bufSize: GLsizei, length: GLsizei_ptr, source: str_ptr) -> None: ...
def glGetShaderiv(shader: GLuint, pname: GLenum, params: GLint_ptr) -> None: ...
def glGetString(name: GLenum) -> str | None: ...
def glGetStringi(name: GLenum, index: GLuint) -> str | None: ...
def glGetTexParameterfv(target: GLenum, pname: GLenum, params: float_ptr) -> None: ...
def glGetTexParameteriv(target: GLenum, pname: GLenum, params: GLint_ptr) -> None: ...
def glGetTransformFeedbackVarying(
    program: GLuint,
    index: GLuint,
    bufSize: GLsizei,
    length: GLsizei_ptr,
    size: GLint_ptr,
    type: GLenum,
    name: str_ptr,
) -> None: ...
def glGetUniformLocation(program: GLuint, name: str) -> GLint: ...
def glGetUniformfv(program: GLuint, location: GLint, params: float_ptr) -> None: ...
def glGetUniformiv(program: GLuint, location: GLint, params: GLint_ptr) -> None: ...
def glGetUniformuiv(program: GLuint, location: GLint, params: GLuint_ptr) -> None: ...
def glGetVertexAttribIiv(index: GLuint, pname: GLenum, params: GLint_ptr) -> None: ...
def glGetVertexAttribIuiv(index: GLuint, pname: GLenum, params: GLuint_ptr) -> None: ...
def glGetVertexAttribPointerv(index: GLuint, pname: GLenum, pointer: GLvoid_ptr_ptr) -> None: ...
def glGetVertexAttribfv(index: GLuint, pname: GLenum, params: float_ptr) -> None: ...
def glGetVertexAttribiv(index: GLuint, pname: GLenum, params: GLint_ptr) -> None: ...
def glHint(target: GLenum, mode: GLenum) -> None: ...
def glIsBuffer(buffer: GLuint) -> bool: ...
def glIsEnabled(cap: GLuint) -> bool: ...
def glIsFramebuffer(framebuffer: GLuint) -> bool: ...
def glIsProgram(program: GLuint) -> bool: ...
def glIsQuery(id: GLuint) -> bool: ...
def glIsRenderbuffer(renderbuffer: GLuint) -> bool: ...
def glIsShader(shader: GLuint) -> bool: ...
def glIsTexture(texture: GLuint) -> bool: ...
def glIsVertexArray(array: GLuint) -> bool: ...
def glLineWidth(width: GLsizei) -> None: ...
def glLinkProgram(program: GLuint) -> None: ...
def glPixelStorei(pname: GLenum, param: GLint) -> None: ...
def glPolygonOffset(factor: float, units: float) -> None: ...
def glReadBuffer(src: GLenum) -> None: ...
def glReadPixels(
    x: GLint,
    y: GLint,
    width: GLsizei,
    height: GLsizei,
    format: GLenum,
    type: GLenum,
    pixels: GLvoid_ptr,
) -> None: ...
def glRenderbufferStorage(target: GLenum, internalformat: GLenum, width: GLsizei, height: GLsizei) -> None: ...
def glRenderbufferStorageMultisample(
    target: GLenum, samples: GLsizei, internalformat: GLenum, width: GLsizei, height: GLsizei
) -> None: ...
def glSampleCoverage(value: float, invert: bool) -> None: ...
def glScissor(x: GLint, y: GLint, width: GLsizei, height: GLsizei) -> None: ...
def glShaderSource(shader: GLuint, count: GLsizei, string: list[str], length: list[GLsizei]) -> None: ...
def glStencilFunc(func: GLenum, ref: GLint, mask: GLuint) -> None: ...
def glStencilFuncSeparate(face: GLenum, func: GLenum, ref: GLint, mask: GLuint) -> None: ...
def glStencilMask(mask: GLuint) -> None: ...
def glStencilMaskSeparate(face: GLenum, mask: GLuint) -> None: ...
def glStencilOp(fail: GLenum, zfail: GLenum, zpass: GLenum) -> None: ...
def glStencilOpSeparate(face: GLenum, sfail: GLenum, dpfail: GLenum, dppass: GLenum) -> None: ...
def glTexImage2D(
    target: GLenum,
    level: GLint,
    internalformat: GLenum,
    width: GLsizei,
    height: GLsizei,
    border: GLint,
    format: GLenum,
    type: GLenum,
    pixels: GLvoid_ptr,
) -> None: ...
def glTexImage3D(
    target: GLenum,
    level: GLint,
    internalformat: GLenum,
    width: GLsizei,
    height: GLsizei,
    depth: GLsizei,
    border: GLint,
    format: GLenum,
    type: GLenum,
    pixels: GLvoid_ptr,
) -> None: ...
def glTexParameterf(target: GLenum, pname: GLenum, param: float) -> None: ...
def glTexParameterfv(target: GLenum, pname: GLenum, params: list[float]) -> None: ...
def glTexParameteri(target: GLenum, pname: GLenum, param: GLint) -> None: ...
def glTexParameteriv(target: GLenum, pname: GLenum, params: list[GLint]) -> None: ...
def glTexSubImage2D(
    target: GLenum,
    level: GLint,
    xoffset: GLint,
    yoffset: GLint,
    width: GLsizei,
    height: GLsizei,
    format: GLenum,
    type: GLenum,
    pixels: GLvoid_ptr,
) -> None: ...
def glTexSubImage3D(
    target: GLenum,
    level: GLint,
    xoffset: GLint,
    yoffset: GLint,
    zoffset: GLint,
    width: GLsizei,
    height: GLsizei,
    depth: GLsizei,
    format: GLenum,
    type: GLenum,
    pixels: GLvoid_ptr,
) -> None: ...
def glTransformFeedbackVaryings(program: GLuint, count: GLsizei, varyings: list[str], bufferMode: GLenum) -> None: ...
def glUniform1f(location: GLint, v0: float) -> None: ...
def glUniform1fv(location: GLint, count: GLsizei, value: list[float]) -> None: ...
def glUniform1i(location: GLint, v0: GLint) -> None: ...
def glUniform1iv(location: GLint, count: GLsizei, value: list[GLint]) -> None: ...
def glUniform1ui(location: GLint, v0: GLuint) -> None: ...
def glUniform1uiv(location: GLint, count: GLsizei, value: list[GLint]) -> None: ...
def glUniform2f(location: GLint, v0: float, v1: float) -> None: ...
def glUniform2fv(location: GLint, count: GLsizei, value: list[float]) -> None: ...
def glUniform2i(location: GLint, v0: GLint, v1: GLint) -> None: ...
def glUniform2iv(location: GLint, count: GLsizei, value: list[GLint]) -> None: ...
def glUniform2ui(location: GLint, v0: GLuint, v1: GLuint) -> None: ...
def glUniform2uiv(location: GLint, count: GLsizei, value: list[GLint]) -> None: ...
def glUniform3f(location: GLint, v0: float, v1: float, v2: float) -> None: ...
def glUniform3fv(location: GLint, count: GLsizei, value: list[float]) -> None: ...
def glUniform3i(location: GLint, v0: GLint, v1: GLint, v2: GLint) -> None: ...
def glUniform3iv(location: GLint, count: GLsizei, value: list[GLint]) -> None: ...
def glUniform3ui(location: GLint, v0: GLuint, v1: GLuint, v2: GLuint) -> None: ...
def glUniform3uiv(location: GLint, count: GLsizei, value: list[GLint]) -> None: ...
def glUniform4f(location: GLint, v0: float, v1: float, v2: float, v3: float) -> None: ...
def glUniform4fv(location: GLint, count: GLsizei, value: list[float]) -> None: ...
def glUniform4i(location: GLint, v0: GLint, v1: GLint, v2: GLint, v3: GLint) -> None: ...
def glUniform4iv(location: GLint, count: GLsizei, value: list[GLint]) -> None: ...
def glUniform4ui(location: GLint, v0: GLuint, v1: GLuint, v2: GLuint, v3: GLuint) -> None: ...
def glUniform4uiv(location: GLint, count: GLsizei, value: list[GLint]) -> None: ...
def glUniformMatrix2fv(location: GLint, count: GLsizei, transpose: bool, value: list[float]) -> None: ...
def glUniformMatrix2x3fv(location: GLint, count: GLsizei, transpose: bool, value: list[float]) -> None: ...
def glUniformMatrix2x4fv(location: GLint, count: GLsizei, transpose: bool, value: list[float]) -> None: ...
def glUniformMatrix3fv(location: GLint, count: GLsizei, transpose: bool, value: list[float]) -> None: ...
def glUniformMatrix3x2fv(location: GLint, count: GLsizei, transpose: bool, value: list[float]) -> None: ...
def glUniformMatrix3x4fv(location: GLint, count: GLsizei, transpose: bool, value: list[float]) -> None: ...
def glUniformMatrix4fv(location: GLint, count: GLsizei, transpose: bool, value: list[float]) -> None: ...
def glUniformMatrix4x2fv(location: GLint, count: GLsizei, transpose: bool, value: list[float]) -> None: ...
def glUniformMatrix4x3fv(location: GLint, count: GLsizei, transpose: bool, value: list[float]) -> None: ...
def glUnmapBuffer(target: GLenum) -> bool: ...
def glUseProgram(program: GLuint) -> None: ...
def glValidateProgram(program: GLuint) -> None: ...
def glVertexAttrib1f(index: GLuint, x: float) -> None: ...
def glVertexAttrib1fv(index: GLuint, v: list[float]) -> None: ...
def glVertexAttrib2f(index: GLuint, x: float, y: float) -> None: ...
def glVertexAttrib2fv(index: GLuint, v: list[float]) -> None: ...
def glVertexAttrib3f(index: GLuint, x: float, y: float, z: float) -> None: ...
def glVertexAttrib3fv(index: GLuint, v: list[float]) -> None: ...
def glVertexAttrib4f(index: GLuint, x: float, y: float, z: float, w: float) -> None: ...
def glVertexAttrib4fv(index: GLuint, v: list[float]) -> None: ...
def glVertexAttribI4i(index: GLuint, x: GLint, y: GLint, z: GLint, w: GLint) -> None: ...
def glVertexAttribI4iv(index: GLuint, v: list[GLint]) -> None: ...
def glVertexAttribI4ui(index: GLuint, x: GLuint, y: GLuint, z: GLuint, w: GLuint) -> None: ...
def glVertexAttribI4uiv(index: GLuint, v: list[GLuint]) -> None: ...
def glVertexAttribIPointer(index: GLuint, size: GLint, type: GLenum, stride: GLsizei, pointer: GLvoid_ptr) -> None: ...
def glVertexAttribPointer(
    index: GLuint,
    size: GLint,
    type: GLenum,
    normalized: bool,
    stride: GLsizei,
    pointer: GLvoid_ptr,
) -> None: ...
def glViewport(x: GLint, y: GLint, width: GLsizei, height: GLsizei) -> None: ...

class ptr:
    def __init__(self, o: object, ro: bool = True) -> None: ...
    def __init__(self, o: object, ro: bool = True) -> None: ...

GL_ACTIVE_ATTRIBUTES: GLenum
GL_ACTIVE_ATTRIBUTE_MAX_LENGTH: GLenum
GL_ACTIVE_TEXTURE: GLenum
GL_ACTIVE_UNIFORMS: GLenum
GL_ACTIVE_UNIFORM_MAX_LENGTH: GLenum
GL_ALIASED_LINE_WIDTH_RANGE: GLenum
GL_ALIASED_POINT_SIZE_RANGE: GLenum
GL_ALPHA: GLenum
GL_ALPHA_BITS: GLenum
GL_ALWAYS: GLenum
GL_ARRAY_BUFFER: GLenum
GL_ARRAY_BUFFER_BINDING: GLenum
GL_ATTACHED_SHADERS: GLenum
GL_BACK: GLenum
GL_BLEND: GLenum
GL_BLEND_COLOR: GLenum
GL_BLEND_DST_ALPHA: GLenum
GL_BLEND_DST_RGB: GLenum
GL_BLEND_EQUATION: GLenum
GL_BLEND_EQUATION_ALPHA: GLenum
GL_BLEND_EQUATION_RGB: GLenum
GL_BLEND_SRC_ALPHA: GLenum
GL_BLEND_SRC_RGB: GLenum
GL_BLUE: GLenum
GL_BLUE_BITS: GLenum
GL_BOOL: GLenum
GL_BOOL_VEC2: GLenum
GL_BOOL_VEC3: GLenum
GL_BOOL_VEC4: GLenum
GL_BUFFER_ACCESS_FLAGS: GLenum
GL_BUFFER_MAPPED: GLenum
GL_BUFFER_MAP_LENGTH: GLenum
GL_BUFFER_MAP_OFFSET: GLenum
GL_BUFFER_MAP_POINTER: GLenum
GL_BUFFER_SIZE: GLenum
GL_BUFFER_USAGE: GLenum
GL_BYTE: GLenum
GL_CCW: GLenum
GL_CLAMP_TO_EDGE: GLenum
GL_COLOR: GLenum
GL_COLOR_ATTACHMENT0: GLenum
GL_COLOR_ATTACHMENT1: GLenum
GL_COLOR_ATTACHMENT10: GLenum
GL_COLOR_ATTACHMENT11: GLenum
GL_COLOR_ATTACHMENT12: GLenum
GL_COLOR_ATTACHMENT13: GLenum
GL_COLOR_ATTACHMENT14: GLenum
GL_COLOR_ATTACHMENT15: GLenum
GL_COLOR_ATTACHMENT16: GLenum
GL_COLOR_ATTACHMENT17: GLenum
GL_COLOR_ATTACHMENT18: GLenum
GL_COLOR_ATTACHMENT19: GLenum
GL_COLOR_ATTACHMENT2: GLenum
GL_COLOR_ATTACHMENT20: GLenum
GL_COLOR_ATTACHMENT21: GLenum
GL_COLOR_ATTACHMENT22: GLenum
GL_COLOR_ATTACHMENT23: GLenum
GL_COLOR_ATTACHMENT24: GLenum
GL_COLOR_ATTACHMENT25: GLenum
GL_COLOR_ATTACHMENT26: GLenum
GL_COLOR_ATTACHMENT27: GLenum
GL_COLOR_ATTACHMENT28: GLenum
GL_COLOR_ATTACHMENT29: GLenum
GL_COLOR_ATTACHMENT3: GLenum
GL_COLOR_ATTACHMENT30: GLenum
GL_COLOR_ATTACHMENT31: GLenum
GL_COLOR_ATTACHMENT4: GLenum
GL_COLOR_ATTACHMENT5: GLenum
GL_COLOR_ATTACHMENT6: GLenum
GL_COLOR_ATTACHMENT7: GLenum
GL_COLOR_ATTACHMENT8: GLenum
GL_COLOR_ATTACHMENT9: GLenum
GL_COLOR_BUFFER_BIT: GLenum
GL_COLOR_CLEAR_VALUE: GLenum
GL_COLOR_WRITEMASK: GLenum
GL_COMPARE_REF_TO_TEXTURE: GLenum
GL_COMPILE_STATUS: GLenum
GL_COMPRESSED_TEXTURE_FORMATS: GLenum
GL_CONSTANT_ALPHA: GLenum
GL_CONSTANT_COLOR: GLenum
GL_CULL_FACE: GLenum
GL_CULL_FACE_MODE: GLenum
GL_CURRENT_PROGRAM: GLenum
GL_CURRENT_QUERY: GLenum
GL_CURRENT_VERTEX_ATTRIB: GLenum
GL_CW: GLenum
GL_DECR: GLenum
GL_DECR_WRAP: GLenum
GL_DELETE_STATUS: GLenum
GL_DEPTH: GLenum
GL_DEPTH24_STENCIL8: GLenum
GL_DEPTH32F_STENCIL8: GLenum
GL_DEPTH_ATTACHMENT: GLenum
GL_DEPTH_BITS: GLenum
GL_DEPTH_BUFFER_BIT: GLenum
GL_DEPTH_CLEAR_VALUE: GLenum
GL_DEPTH_COMPONENT: GLenum
GL_DEPTH_COMPONENT16: GLenum
GL_DEPTH_COMPONENT24: GLenum
GL_DEPTH_COMPONENT32F: GLenum
GL_DEPTH_FUNC: GLenum
GL_DEPTH_RANGE: GLenum
GL_DEPTH_STENCIL: GLenum
GL_DEPTH_STENCIL_ATTACHMENT: GLenum
GL_DEPTH_TEST: GLenum
GL_DEPTH_WRITEMASK: GLenum
GL_DITHER: GLenum
GL_DONT_CARE: GLenum
GL_DRAW_BUFFER0: GLenum
GL_DRAW_BUFFER1: GLenum
GL_DRAW_BUFFER10: GLenum
GL_DRAW_BUFFER11: GLenum
GL_DRAW_BUFFER12: GLenum
GL_DRAW_BUFFER13: GLenum
GL_DRAW_BUFFER14: GLenum
GL_DRAW_BUFFER15: GLenum
GL_DRAW_BUFFER2: GLenum
GL_DRAW_BUFFER3: GLenum
GL_DRAW_BUFFER4: GLenum
GL_DRAW_BUFFER5: GLenum
GL_DRAW_BUFFER6: GLenum
GL_DRAW_BUFFER7: GLenum
GL_DRAW_BUFFER8: GLenum
GL_DRAW_BUFFER9: GLenum
GL_DRAW_FRAMEBUFFER: GLenum
GL_DRAW_FRAMEBUFFER_BINDING: GLenum
GL_DST_ALPHA: GLenum
GL_DST_COLOR: GLenum
GL_DYNAMIC_COPY: GLenum
GL_DYNAMIC_DRAW: GLenum
GL_DYNAMIC_READ: GLenum
GL_ELEMENT_ARRAY_BUFFER: GLenum
GL_ELEMENT_ARRAY_BUFFER_BINDING: GLenum
GL_EQUAL: GLenum
GL_EXTENSIONS: GLenum
GL_FALSE: GLenum
GL_FASTEST: GLenum
GL_FLOAT: GLenum
GL_FLOAT_32_UNSIGNED_INT_24_8_REV: GLenum
GL_FLOAT_MAT2: GLenum
GL_FLOAT_MAT2x3: GLenum
GL_FLOAT_MAT2x4: GLenum
GL_FLOAT_MAT3: GLenum
GL_FLOAT_MAT3x2: GLenum
GL_FLOAT_MAT3x4: GLenum
GL_FLOAT_MAT4: GLenum
GL_FLOAT_MAT4x2: GLenum
GL_FLOAT_MAT4x3: GLenum
GL_FLOAT_VEC2: GLenum
GL_FLOAT_VEC3: GLenum
GL_FLOAT_VEC4: GLenum
GL_FRAGMENT_SHADER: GLenum
GL_FRAGMENT_SHADER_DERIVATIVE_HINT: GLenum
GL_FRAMEBUFFER: GLenum
GL_FRAMEBUFFER_ATTACHMENT_ALPHA_SIZE: GLenum
GL_FRAMEBUFFER_ATTACHMENT_BLUE_SIZE: GLenum
GL_FRAMEBUFFER_ATTACHMENT_COLOR_ENCODING: GLenum
GL_FRAMEBUFFER_ATTACHMENT_COMPONENT_TYPE: GLenum
GL_FRAMEBUFFER_ATTACHMENT_DEPTH_SIZE: GLenum
GL_FRAMEBUFFER_ATTACHMENT_GREEN_SIZE: GLenum
GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME: GLenum
GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE: GLenum
GL_FRAMEBUFFER_ATTACHMENT_RED_SIZE: GLenum
GL_FRAMEBUFFER_ATTACHMENT_STENCIL_SIZE: GLenum
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE: GLenum
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LAYER: GLenum
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL: GLenum
GL_FRAMEBUFFER_BINDING: GLenum
GL_FRAMEBUFFER_COMPLETE: GLenum
GL_FRAMEBUFFER_DEFAULT: GLenum
GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT: GLenum
GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT: GLenum
GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE: GLenum
GL_FRAMEBUFFER_UNDEFINED: GLenum
GL_FRAMEBUFFER_UNSUPPORTED: GLenum
GL_FRONT: GLenum
GL_FRONT_AND_BACK: GLenum
GL_FRONT_FACE: GLenum
GL_FUNC_ADD: GLenum
GL_FUNC_REVERSE_SUBTRACT: GLenum
GL_FUNC_SUBTRACT: GLenum
GL_GENERATE_MIPMAP_HINT: GLenum
GL_GEQUAL: GLenum
GL_GREATER: GLenum
GL_GREEN: GLenum
GL_GREEN_BITS: GLenum
GL_HALF_FLOAT: GLenum
GL_INCR: GLenum
GL_INCR_WRAP: GLenum
GL_INFO_LOG_LENGTH: GLenum
GL_INT: GLenum
GL_INTERLEAVED_ATTRIBS: GLenum
GL_INT_SAMPLER_2D: GLenum
GL_INT_SAMPLER_2D_ARRAY: GLenum
GL_INT_SAMPLER_3D: GLenum
GL_INT_SAMPLER_CUBE: GLenum
GL_INT_VEC2: GLenum
GL_INT_VEC3: GLenum
GL_INT_VEC4: GLenum
GL_INVALID_ENUM: GLenum
GL_INVALID_FRAMEBUFFER_OPERATION: GLenum
GL_INVALID_OPERATION: GLenum
GL_INVALID_VALUE: GLenum
GL_INVERT: GLenum
GL_KEEP: GLenum
GL_LEQUAL: GLenum
GL_LESS: GLenum
GL_LINEAR: GLenum
GL_LINEAR_MIPMAP_LINEAR: GLenum
GL_LINEAR_MIPMAP_NEAREST: GLenum
GL_LINES: GLenum
GL_LINE_LOOP: GLenum
GL_LINE_STRIP: GLenum
GL_LINE_WIDTH: GLenum
GL_LINK_STATUS: GLenum
GL_LUMINANCE: GLenum
GL_LUMINANCE_ALPHA: GLenum
GL_MAJOR_VERSION: GLenum
GL_MAP_FLUSH_EXPLICIT_BIT: GLenum
GL_MAP_INVALIDATE_BUFFER_BIT: GLenum
GL_MAP_INVALIDATE_RANGE_BIT: GLenum
GL_MAP_READ_BIT: GLenum
GL_MAP_UNSYNCHRONIZED_BIT: GLenum
GL_MAP_WRITE_BIT: GLenum
GL_MAX: GLenum
GL_MAX_3D_TEXTURE_SIZE: GLenum
GL_MAX_ARRAY_TEXTURE_LAYERS: GLenum
GL_MAX_COLOR_ATTACHMENTS: GLenum
GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS: GLenum
GL_MAX_CUBE_MAP_TEXTURE_SIZE: GLenum
GL_MAX_DRAW_BUFFERS: GLenum
GL_MAX_ELEMENTS_INDICES: GLenum
GL_MAX_ELEMENTS_VERTICES: GLenum
GL_MAX_FRAGMENT_UNIFORM_COMPONENTS: GLenum
GL_MAX_PROGRAM_TEXEL_OFFSET: GLenum
GL_MAX_RENDERBUFFER_SIZE: GLenum
GL_MAX_SAMPLES: GLenum
GL_MAX_TEXTURE_IMAGE_UNITS: GLenum
GL_MAX_TEXTURE_LOD_BIAS: GLenum
GL_MAX_TEXTURE_SIZE: GLenum
GL_MAX_TRANSFORM_FEEDBACK_INTERLEAVED_COMPONENTS: GLenum
GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_ATTRIBS: GLenum
GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_COMPONENTS: GLenum
GL_MAX_VARYING_COMPONENTS: GLenum
GL_MAX_VERTEX_ATTRIBS: GLenum
GL_MAX_VERTEX_TEXTURE_IMAGE_UNITS: GLenum
GL_MAX_VERTEX_UNIFORM_COMPONENTS: GLenum
GL_MAX_VIEWPORT_DIMS: GLenum
GL_MIN: GLenum
GL_MINOR_VERSION: GLenum
GL_MIN_PROGRAM_TEXEL_OFFSET: GLenum
GL_MIRRORED_REPEAT: GLenum
GL_NEAREST: GLenum
GL_NEAREST_MIPMAP_LINEAR: GLenum
GL_NEAREST_MIPMAP_NEAREST: GLenum
GL_NEVER: GLenum
GL_NICEST: GLenum
GL_NONE: GLenum
GL_NOTEQUAL: GLenum
GL_NO_ERROR: GLenum
GL_NUM_COMPRESSED_TEXTURE_FORMATS: GLenum
GL_NUM_EXTENSIONS: GLenum
GL_ONE: GLenum
GL_ONE_MINUS_CONSTANT_ALPHA: GLenum
GL_ONE_MINUS_CONSTANT_COLOR: GLenum
GL_ONE_MINUS_DST_ALPHA: GLenum
GL_ONE_MINUS_DST_COLOR: GLenum
GL_ONE_MINUS_SRC_ALPHA: GLenum
GL_ONE_MINUS_SRC_COLOR: GLenum
GL_OUT_OF_MEMORY: GLenum
GL_PACK_ALIGNMENT: GLenum
GL_PACK_ROW_LENGTH: GLenum
GL_PACK_SKIP_PIXELS: GLenum
GL_PACK_SKIP_ROWS: GLenum
GL_PIXEL_PACK_BUFFER: GLenum
GL_PIXEL_PACK_BUFFER_BINDING: GLenum
GL_PIXEL_UNPACK_BUFFER: GLenum
GL_PIXEL_UNPACK_BUFFER_BINDING: GLenum
GL_POINTS: GLenum
GL_POLYGON_OFFSET_FACTOR: GLenum
GL_POLYGON_OFFSET_FILL: GLenum
GL_POLYGON_OFFSET_UNITS: GLenum
GL_QUERY_RESULT: GLenum
GL_QUERY_RESULT_AVAILABLE: GLenum
GL_R11F_G11F_B10F: GLenum
GL_R16F: GLenum
GL_R16I: GLenum
GL_R16UI: GLenum
GL_R32F: GLenum
GL_R32I: GLenum
GL_R32UI: GLenum
GL_R8: GLenum
GL_R8I: GLenum
GL_R8UI: GLenum
GL_RASTERIZER_DISCARD: GLenum
GL_READ_BUFFER: GLenum
GL_READ_FRAMEBUFFER: GLenum
GL_READ_FRAMEBUFFER_BINDING: GLenum
GL_RED: GLenum
GL_RED_BITS: GLenum
GL_RED_INTEGER: GLenum
GL_RENDERBUFFER: GLenum
GL_RENDERBUFFER_ALPHA_SIZE: GLenum
GL_RENDERBUFFER_BINDING: GLenum
GL_RENDERBUFFER_BLUE_SIZE: GLenum
GL_RENDERBUFFER_DEPTH_SIZE: GLenum
GL_RENDERBUFFER_GREEN_SIZE: GLenum
GL_RENDERBUFFER_HEIGHT: GLenum
GL_RENDERBUFFER_INTERNAL_FORMAT: GLenum
GL_RENDERBUFFER_RED_SIZE: GLenum
GL_RENDERBUFFER_SAMPLES: GLenum
GL_RENDERBUFFER_STENCIL_SIZE: GLenum
GL_RENDERBUFFER_WIDTH: GLenum
GL_RENDERER: GLenum
GL_REPEAT: GLenum
GL_REPLACE: GLenum
GL_RG: GLenum
GL_RG16F: GLenum
GL_RG16I: GLenum
GL_RG16UI: GLenum
GL_RG32F: GLenum
GL_RG32I: GLenum
GL_RG32UI: GLenum
GL_RG8: GLenum
GL_RG8I: GLenum
GL_RG8UI: GLenum
GL_RGB: GLenum
GL_RGB10_A2: GLenum
GL_RGB16F: GLenum
GL_RGB16I: GLenum
GL_RGB16UI: GLenum
GL_RGB32F: GLenum
GL_RGB32I: GLenum
GL_RGB32UI: GLenum
GL_RGB5_A1: GLenum
GL_RGB8: GLenum
GL_RGB8I: GLenum
GL_RGB8UI: GLenum
GL_RGB9_E5: GLenum
GL_RGBA: GLenum
GL_RGBA16F: GLenum
GL_RGBA16I: GLenum
GL_RGBA16UI: GLenum
GL_RGBA32F: GLenum
GL_RGBA32I: GLenum
GL_RGBA32UI: GLenum
GL_RGBA4: GLenum
GL_RGBA8: GLenum
GL_RGBA8I: GLenum
GL_RGBA8UI: GLenum
GL_RGBA_INTEGER: GLenum
GL_RGB_INTEGER: GLenum
GL_RG_INTEGER: GLenum
GL_SAMPLER_2D: GLenum
GL_SAMPLER_2D_ARRAY: GLenum
GL_SAMPLER_2D_ARRAY_SHADOW: GLenum
GL_SAMPLER_2D_SHADOW: GLenum
GL_SAMPLER_3D: GLenum
GL_SAMPLER_CUBE: GLenum
GL_SAMPLER_CUBE_SHADOW: GLenum
GL_SAMPLES: GLenum
GL_SAMPLE_ALPHA_TO_COVERAGE: GLenum
GL_SAMPLE_BUFFERS: GLenum
GL_SAMPLE_COVERAGE: GLenum
GL_SAMPLE_COVERAGE_INVERT: GLenum
GL_SAMPLE_COVERAGE_VALUE: GLenum
GL_SCISSOR_BOX: GLenum
GL_SCISSOR_TEST: GLenum
GL_SEPARATE_ATTRIBS: GLenum
GL_SHADER_SOURCE_LENGTH: GLenum
GL_SHADER_TYPE: GLenum
GL_SHADING_LANGUAGE_VERSION: GLenum
GL_SHORT: GLenum
GL_SRC_ALPHA: GLenum
GL_SRC_ALPHA_SATURATE: GLenum
GL_SRC_COLOR: GLenum
GL_SRGB: GLenum
GL_SRGB8: GLenum
GL_SRGB8_ALPHA8: GLenum
GL_STATIC_COPY: GLenum
GL_STATIC_DRAW: GLenum
GL_STATIC_READ: GLenum
GL_STENCIL: GLenum
GL_STENCIL_ATTACHMENT: GLenum
GL_STENCIL_BACK_FAIL: GLenum
GL_STENCIL_BACK_FUNC: GLenum
GL_STENCIL_BACK_PASS_DEPTH_FAIL: GLenum
GL_STENCIL_BACK_PASS_DEPTH_PASS: GLenum
GL_STENCIL_BACK_REF: GLenum
GL_STENCIL_BACK_VALUE_MASK: GLenum
GL_STENCIL_BACK_WRITEMASK: GLenum
GL_STENCIL_BITS: GLenum
GL_STENCIL_BUFFER_BIT: GLenum
GL_STENCIL_CLEAR_VALUE: GLenum
GL_STENCIL_FAIL: GLenum
GL_STENCIL_FUNC: GLenum
GL_STENCIL_INDEX8: GLenum
GL_STENCIL_PASS_DEPTH_FAIL: GLenum
GL_STENCIL_PASS_DEPTH_PASS: GLenum
GL_STENCIL_REF: GLenum
GL_STENCIL_TEST: GLenum
GL_STENCIL_VALUE_MASK: GLenum
GL_STENCIL_WRITEMASK: GLenum
GL_STREAM_COPY: GLenum
GL_STREAM_DRAW: GLenum
GL_STREAM_READ: GLenum
GL_SUBPIXEL_BITS: GLenum
GL_TEXTURE: GLenum
GL_TEXTURE0: GLenum
GL_TEXTURE1: GLenum
GL_TEXTURE10: GLenum
GL_TEXTURE11: GLenum
GL_TEXTURE12: GLenum
GL_TEXTURE13: GLenum
GL_TEXTURE14: GLenum
GL_TEXTURE15: GLenum
GL_TEXTURE16: GLenum
GL_TEXTURE17: GLenum
GL_TEXTURE18: GLenum
GL_TEXTURE19: GLenum
GL_TEXTURE2: GLenum
GL_TEXTURE20: GLenum
GL_TEXTURE21: GLenum
GL_TEXTURE22: GLenum
GL_TEXTURE23: GLenum
GL_TEXTURE24: GLenum
GL_TEXTURE25: GLenum
GL_TEXTURE26: GLenum
GL_TEXTURE27: GLenum
GL_TEXTURE28: GLenum
GL_TEXTURE29: GLenum
GL_TEXTURE3: GLenum
GL_TEXTURE30: GLenum
GL_TEXTURE31: GLenum
GL_TEXTURE4: GLenum
GL_TEXTURE5: GLenum
GL_TEXTURE6: GLenum
GL_TEXTURE7: GLenum
GL_TEXTURE8: GLenum
GL_TEXTURE9: GLenum
GL_TEXTURE_2D: GLenum
GL_TEXTURE_2D_ARRAY: GLenum
GL_TEXTURE_3D: GLenum
GL_TEXTURE_BASE_LEVEL: GLenum
GL_TEXTURE_BINDING_2D: GLenum
GL_TEXTURE_BINDING_2D_ARRAY: GLenum
GL_TEXTURE_BINDING_3D: GLenum
GL_TEXTURE_BINDING_CUBE_MAP: GLenum
GL_TEXTURE_COMPARE_FUNC: GLenum
GL_TEXTURE_COMPARE_MODE: GLenum
GL_TEXTURE_CUBE_MAP: GLenum
GL_TEXTURE_CUBE_MAP_NEGATIVE_X: GLenum
GL_TEXTURE_CUBE_MAP_NEGATIVE_Y: GLenum
GL_TEXTURE_CUBE_MAP_NEGATIVE_Z: GLenum
GL_TEXTURE_CUBE_MAP_POSITIVE_X: GLenum
GL_TEXTURE_CUBE_MAP_POSITIVE_Y: GLenum
GL_TEXTURE_CUBE_MAP_POSITIVE_Z: GLenum
GL_TEXTURE_MAG_FILTER: GLenum
GL_TEXTURE_MAX_LEVEL: GLenum
GL_TEXTURE_MAX_LOD: GLenum
GL_TEXTURE_MIN_FILTER: GLenum
GL_TEXTURE_MIN_LOD: GLenum
GL_TEXTURE_WRAP_R: GLenum
GL_TEXTURE_WRAP_S: GLenum
GL_TEXTURE_WRAP_T: GLenum
GL_TRANSFORM_FEEDBACK_BUFFER: GLenum
GL_TRANSFORM_FEEDBACK_BUFFER_BINDING: GLenum
GL_TRANSFORM_FEEDBACK_BUFFER_MODE: GLenum
GL_TRANSFORM_FEEDBACK_BUFFER_SIZE: GLenum
GL_TRANSFORM_FEEDBACK_BUFFER_START: GLenum
GL_TRANSFORM_FEEDBACK_PRIMITIVES_WRITTEN: GLenum
GL_TRANSFORM_FEEDBACK_VARYINGS: GLenum
GL_TRANSFORM_FEEDBACK_VARYING_MAX_LENGTH: GLenum
GL_TRIANGLES: GLenum
GL_TRIANGLE_FAN: GLenum
GL_TRIANGLE_STRIP: GLenum
GL_TRUE: GLenum
GL_UNPACK_ALIGNMENT: GLenum
GL_UNPACK_IMAGE_HEIGHT: GLenum
GL_UNPACK_ROW_LENGTH: GLenum
GL_UNPACK_SKIP_IMAGES: GLenum
GL_UNPACK_SKIP_PIXELS: GLenum
GL_UNPACK_SKIP_ROWS: GLenum
GL_UNSIGNED_BYTE: GLenum
GL_UNSIGNED_INT: GLenum
GL_UNSIGNED_INT_10F_11F_11F_REV: GLenum
GL_UNSIGNED_INT_24_8: GLenum
GL_UNSIGNED_INT_2_10_10_10_REV: GLenum
GL_UNSIGNED_INT_5_9_9_9_REV: GLenum
GL_UNSIGNED_INT_SAMPLER_2D: GLenum
GL_UNSIGNED_INT_SAMPLER_2D_ARRAY: GLenum
GL_UNSIGNED_INT_SAMPLER_3D: GLenum
GL_UNSIGNED_INT_SAMPLER_CUBE: GLenum
GL_UNSIGNED_INT_VEC2: GLenum
GL_UNSIGNED_INT_VEC3: GLenum
GL_UNSIGNED_INT_VEC4: GLenum
GL_UNSIGNED_NORMALIZED: GLenum
GL_UNSIGNED_SHORT: GLenum
GL_UNSIGNED_SHORT_4_4_4_4: GLenum
GL_UNSIGNED_SHORT_5_5_5_1: GLenum
GL_UNSIGNED_SHORT_5_6_5: GLenum
GL_VALIDATE_STATUS: GLenum
GL_VENDOR: GLenum
GL_VERSION: GLenum
GL_VERTEX_ARRAY_BINDING: GLenum
GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING: GLenum
GL_VERTEX_ATTRIB_ARRAY_ENABLED: GLenum
GL_VERTEX_ATTRIB_ARRAY_INTEGER: GLenum
GL_VERTEX_ATTRIB_ARRAY_NORMALIZED: GLenum
GL_VERTEX_ATTRIB_ARRAY_POINTER: GLenum
GL_VERTEX_ATTRIB_ARRAY_SIZE: GLenum
GL_VERTEX_ATTRIB_ARRAY_STRIDE: GLenum
GL_VERTEX_ATTRIB_ARRAY_TYPE: GLenum
GL_VERTEX_SHADER: GLenum
GL_VIEWPORT: GLenum
GL_ZERO: GLenum
