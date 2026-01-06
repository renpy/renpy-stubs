from _frozen_importlib import BuiltinImporter as BuiltinImporter
from _typeshed import Incomplete

class Buffer:
    def __buffer__(self, flags: Incomplete) -> None: ...
    def __reduce__(self) -> None: ...
    def __release_buffer__(self, buffer: Incomplete) -> None: ...

class BytesBuffer(Buffer):
    def __init__(self, /, *args, **kwargs) -> None: ...
    def __reduce__(self) -> None: ...
    def get(self) -> None: ...

class BytesListBuffer(Buffer):
    def __init__(self, /, *args, **kwargs) -> None: ...
    def __reduce__(self) -> None: ...

class FloatBuffer(Buffer):
    def __init__(self, /, *args, **kwargs) -> None: ...
    def __getitem__(self, key: Incomplete) -> None: ...
    def __reduce__(self) -> None: ...

class IntBuffer(Buffer):
    def __init__(self, /, *args, **kwargs) -> None: ...
    def __getitem__(self, key: Incomplete) -> None: ...
    def __reduce__(self) -> None: ...

def glActiveTexture(texture: Incomplete) -> None: ...
def glAttachShader(program: Incomplete, shader: Incomplete) -> None: ...
def glBeginQuery(target: Incomplete, id: Incomplete) -> None: ...
def glBeginTransformFeedback(primitiveMode: Incomplete) -> None: ...
def glBindAttribLocation(program: Incomplete, index: Incomplete, name: Incomplete) -> None: ...
def glBindBuffer(target: Incomplete, buffer: Incomplete) -> None: ...
def glBindBufferBase(target: Incomplete, index: Incomplete, buffer: Incomplete) -> None: ...
def glBindBufferRange(
    target: Incomplete, index: Incomplete, buffer: Incomplete, offset: Incomplete, size: Incomplete
) -> None: ...
def glBindFramebuffer(target: Incomplete, framebuffer: Incomplete) -> None: ...
def glBindRenderbuffer(target: Incomplete, renderbuffer: Incomplete) -> None: ...
def glBindTexture(target: Incomplete, texture: Incomplete) -> None: ...
def glBindVertexArray(array: Incomplete) -> None: ...
def glBlendColor(red: Incomplete, green: Incomplete, blue: Incomplete, alpha: Incomplete) -> None: ...
def glBlendEquation(mode: Incomplete) -> None: ...
def glBlendEquationSeparate(modeRGB: Incomplete, modeAlpha: Incomplete) -> None: ...
def glBlendFunc(sfactor: Incomplete, dfactor: Incomplete) -> None: ...
def glBlendFuncSeparate(
    sfactorRGB: Incomplete, dfactorRGB: Incomplete, sfactorAlpha: Incomplete, dfactorAlpha: Incomplete
) -> None: ...
def glBlitFramebuffer(
    srcX0: Incomplete,
    srcY0: Incomplete,
    srcX1: Incomplete,
    srcY1: Incomplete,
    dstX0: Incomplete,
    dstY0: Incomplete,
    dstX1: Incomplete,
    dstY1: Incomplete,
    mask: Incomplete,
    filter: Incomplete,
) -> None: ...
def glBufferData(target: Incomplete, size: Incomplete, data: Incomplete, usage: Incomplete) -> None: ...
def glBufferSubData(target: Incomplete, offset: Incomplete, size: Incomplete, data: Incomplete) -> None: ...
def glCheckFramebufferStatus(target: Incomplete) -> None: ...
def glClear(mask: Incomplete) -> None: ...
def glClearBufferfi(buffer: Incomplete, drawbuffer: Incomplete, depth: Incomplete, stencil: Incomplete) -> None: ...
def glClearBufferfv(buffer: Incomplete, drawbuffer: Incomplete, value: Incomplete) -> None: ...
def glClearBufferiv(buffer: Incomplete, drawbuffer: Incomplete, value: Incomplete) -> None: ...
def glClearBufferuiv(buffer: Incomplete, drawbuffer: Incomplete, value: Incomplete) -> None: ...
def glClearColor(red: Incomplete, green: Incomplete, blue: Incomplete, alpha: Incomplete) -> None: ...
def glClearStencil(s: Incomplete) -> None: ...
def glColorMask(red: Incomplete, green: Incomplete, blue: Incomplete, alpha: Incomplete) -> None: ...
def glCompileShader(shader: Incomplete) -> None: ...
def glCompressedTexImage2D(
    target: Incomplete,
    level: Incomplete,
    internalformat: Incomplete,
    width: Incomplete,
    height: Incomplete,
    border: Incomplete,
    imageSize: Incomplete,
    data: Incomplete,
) -> None: ...
def glCompressedTexImage3D(
    target: Incomplete,
    level: Incomplete,
    internalformat: Incomplete,
    width: Incomplete,
    height: Incomplete,
    depth: Incomplete,
    border: Incomplete,
    imageSize: Incomplete,
    data: Incomplete,
) -> None: ...
def glCompressedTexSubImage2D(
    target: Incomplete,
    level: Incomplete,
    xoffset: Incomplete,
    yoffset: Incomplete,
    width: Incomplete,
    height: Incomplete,
    format: Incomplete,
    imageSize: Incomplete,
    data: Incomplete,
) -> None: ...
def glCompressedTexSubImage3D(
    target: Incomplete,
    level: Incomplete,
    xoffset: Incomplete,
    yoffset: Incomplete,
    zoffset: Incomplete,
    width: Incomplete,
    height: Incomplete,
    depth: Incomplete,
    format: Incomplete,
    imageSize: Incomplete,
    data: Incomplete,
) -> None: ...
def glCopyTexImage2D(
    target: Incomplete,
    level: Incomplete,
    internalformat: Incomplete,
    x: Incomplete,
    y: Incomplete,
    width: Incomplete,
    height: Incomplete,
    border: Incomplete,
) -> None: ...
def glCopyTexSubImage2D(
    target: Incomplete,
    level: Incomplete,
    xoffset: Incomplete,
    yoffset: Incomplete,
    x: Incomplete,
    y: Incomplete,
    width: Incomplete,
    height: Incomplete,
) -> None: ...
def glCopyTexSubImage3D(
    target: Incomplete,
    level: Incomplete,
    xoffset: Incomplete,
    yoffset: Incomplete,
    zoffset: Incomplete,
    x: Incomplete,
    y: Incomplete,
    width: Incomplete,
    height: Incomplete,
    depth: Incomplete,
) -> None: ...
def glCreateProgram() -> None: ...
def glCreateShader(type: Incomplete) -> None: ...
def glCullFace(mode: Incomplete) -> None: ...
def glDeleteBuffers(n: Incomplete, buffers: Incomplete) -> None: ...
def glDeleteFramebuffers(n: Incomplete, framebuffers: Incomplete) -> None: ...
def glDeleteProgram(program: Incomplete) -> None: ...
def glDeleteQueries(n: Incomplete, ids: Incomplete) -> None: ...
def glDeleteRenderbuffers(n: Incomplete, renderbuffers: Incomplete) -> None: ...
def glDeleteShader(shader: Incomplete) -> None: ...
def glDeleteTextures(n: Incomplete, textures: Incomplete) -> None: ...
def glDeleteVertexArrays(n: Incomplete, arrays: Incomplete) -> None: ...
def glDepthFunc(func: Incomplete) -> None: ...
def glDepthMask(flag: Incomplete) -> None: ...
def glDetachShader(program: Incomplete, shader: Incomplete) -> None: ...
def glDisable(cap: Incomplete) -> None: ...
def glDisableVertexAttribArray(index: Incomplete) -> None: ...
def glDrawArrays(mode: Incomplete, first: Incomplete, count: Incomplete) -> None: ...
def glDrawBuffers(n: Incomplete, bufs: Incomplete) -> None: ...
def glDrawElements(mode: Incomplete, count: Incomplete, type: Incomplete, indices: Incomplete) -> None: ...
def glDrawRangeElements(
    mode: Incomplete, start: Incomplete, end: Incomplete, count: Incomplete, type: Incomplete, indices: Incomplete
) -> None: ...
def glEnable(cap: Incomplete) -> None: ...
def glEnableVertexAttribArray(index: Incomplete) -> None: ...
def glEndQuery(target: Incomplete) -> None: ...
def glEndTransformFeedback() -> None: ...
def glFinish() -> None: ...
def glFlush() -> None: ...
def glFlushMappedBufferRange(target: Incomplete, offset: Incomplete, length: Incomplete) -> None: ...
def glFramebufferRenderbuffer(
    target: Incomplete, attachment: Incomplete, renderbuffertarget: Incomplete, renderbuffer: Incomplete
) -> None: ...
def glFramebufferTexture2D(
    target: Incomplete, attachment: Incomplete, textarget: Incomplete, texture: Incomplete, level: Incomplete
) -> None: ...
def glFramebufferTextureLayer(
    target: Incomplete, attachment: Incomplete, texture: Incomplete, level: Incomplete, layer: Incomplete
) -> None: ...
def glFrontFace(mode: Incomplete) -> None: ...
def glGenBuffers(n: Incomplete, buffers: Incomplete) -> None: ...
def glGenFramebuffers(n: Incomplete, framebuffers: Incomplete) -> None: ...
def glGenQueries(n: Incomplete, ids: Incomplete) -> None: ...
def glGenRenderbuffers(n: Incomplete, renderbuffers: Incomplete) -> None: ...
def glGenTextures(n: Incomplete, textures: Incomplete) -> None: ...
def glGenVertexArrays(n: Incomplete, arrays: Incomplete) -> None: ...
def glGenerateMipmap(target: Incomplete) -> None: ...
def glGetActiveAttrib(
    program: Incomplete,
    index: Incomplete,
    bufSize: Incomplete,
    length: Incomplete,
    size: Incomplete,
    type: Incomplete,
    name: Incomplete,
) -> None: ...
def glGetActiveUniform(
    program: Incomplete,
    index: Incomplete,
    bufSize: Incomplete,
    length: Incomplete,
    size: Incomplete,
    type: Incomplete,
    name: Incomplete,
) -> None: ...
def glGetAttachedShaders(program: Incomplete, maxCount: Incomplete, count: Incomplete, shaders: Incomplete) -> None: ...
def glGetAttribLocation(program: Incomplete, name: Incomplete) -> None: ...
def glGetBooleanv(pname: Incomplete, data: Incomplete) -> None: ...
def glGetBufferParameteriv(target: Incomplete, pname: Incomplete, params: Incomplete) -> None: ...
def glGetBufferPointerv(target: Incomplete, pname: Incomplete, params: Incomplete) -> None: ...
def glGetError() -> None: ...
def glGetFloatv(pname: Incomplete, data: Incomplete) -> None: ...
def glGetFragDataLocation(program: Incomplete, name: Incomplete) -> None: ...
def glGetFramebufferAttachmentParameteriv(
    target: Incomplete, attachment: Incomplete, pname: Incomplete, params: Incomplete
) -> None: ...
def glGetIntegeri_v(target: Incomplete, index: Incomplete, data: Incomplete) -> None: ...
def glGetIntegerv(pname: Incomplete, data: Incomplete) -> None: ...
def glGetProgramInfoLog(program: Incomplete, bufSize: Incomplete, length: Incomplete, infoLog: Incomplete) -> None: ...
def glGetProgramiv(program: Incomplete, pname: Incomplete, params: Incomplete) -> None: ...
def glGetQueryObjectuiv(id: Incomplete, pname: Incomplete, params: Incomplete) -> None: ...
def glGetQueryiv(target: Incomplete, pname: Incomplete, params: Incomplete) -> None: ...
def glGetRenderbufferParameteriv(target: Incomplete, pname: Incomplete, params: Incomplete) -> None: ...
def glGetShaderInfoLog(shader: Incomplete, bufSize: Incomplete, length: Incomplete, infoLog: Incomplete) -> None: ...
def glGetShaderSource(shader: Incomplete, bufSize: Incomplete, length: Incomplete, source: Incomplete) -> None: ...
def glGetShaderiv(shader: Incomplete, pname: Incomplete, params: Incomplete) -> None: ...
def glGetString(name: Incomplete) -> None: ...
def glGetStringi(name: Incomplete, index: Incomplete) -> None: ...
def glGetTexParameterfv(target: Incomplete, pname: Incomplete, params: Incomplete) -> None: ...
def glGetTexParameteriv(target: Incomplete, pname: Incomplete, params: Incomplete) -> None: ...
def glGetTransformFeedbackVarying(
    program: Incomplete,
    index: Incomplete,
    bufSize: Incomplete,
    length: Incomplete,
    size: Incomplete,
    type: Incomplete,
    name: Incomplete,
) -> None: ...
def glGetUniformLocation(program: Incomplete, name: Incomplete) -> None: ...
def glGetUniformfv(program: Incomplete, location: Incomplete, params: Incomplete) -> None: ...
def glGetUniformiv(program: Incomplete, location: Incomplete, params: Incomplete) -> None: ...
def glGetUniformuiv(program: Incomplete, location: Incomplete, params: Incomplete) -> None: ...
def glGetVertexAttribIiv(index: Incomplete, pname: Incomplete, params: Incomplete) -> None: ...
def glGetVertexAttribIuiv(index: Incomplete, pname: Incomplete, params: Incomplete) -> None: ...
def glGetVertexAttribPointerv(index: Incomplete, pname: Incomplete, pointer: Incomplete) -> None: ...
def glGetVertexAttribfv(index: Incomplete, pname: Incomplete, params: Incomplete) -> None: ...
def glGetVertexAttribiv(index: Incomplete, pname: Incomplete, params: Incomplete) -> None: ...
def glHint(target: Incomplete, mode: Incomplete) -> None: ...
def glIsBuffer(buffer: Incomplete) -> None: ...
def glIsEnabled(cap: Incomplete) -> None: ...
def glIsFramebuffer(framebuffer: Incomplete) -> None: ...
def glIsProgram(program: Incomplete) -> None: ...
def glIsQuery(id: Incomplete) -> None: ...
def glIsRenderbuffer(renderbuffer: Incomplete) -> None: ...
def glIsShader(shader: Incomplete) -> None: ...
def glIsTexture(texture: Incomplete) -> None: ...
def glIsVertexArray(array: Incomplete) -> None: ...
def glLineWidth(width: Incomplete) -> None: ...
def glLinkProgram(program: Incomplete) -> None: ...
def glPixelStorei(pname: Incomplete, param: Incomplete) -> None: ...
def glPolygonOffset(factor: Incomplete, units: Incomplete) -> None: ...
def glReadBuffer(src: Incomplete) -> None: ...
def glReadPixels(
    x: Incomplete,
    y: Incomplete,
    width: Incomplete,
    height: Incomplete,
    format: Incomplete,
    type: Incomplete,
    pixels: Incomplete,
) -> None: ...
def glRenderbufferStorage(
    target: Incomplete, internalformat: Incomplete, width: Incomplete, height: Incomplete
) -> None: ...
def glRenderbufferStorageMultisample(
    target: Incomplete, samples: Incomplete, internalformat: Incomplete, width: Incomplete, height: Incomplete
) -> None: ...
def glSampleCoverage(value: Incomplete, invert: Incomplete) -> None: ...
def glScissor(x: Incomplete, y: Incomplete, width: Incomplete, height: Incomplete) -> None: ...
def glShaderSource(shader: Incomplete, count: Incomplete, string: Incomplete, length: Incomplete) -> None: ...
def glStencilFunc(func: Incomplete, ref: Incomplete, mask: Incomplete) -> None: ...
def glStencilFuncSeparate(face: Incomplete, func: Incomplete, ref: Incomplete, mask: Incomplete) -> None: ...
def glStencilMask(mask: Incomplete) -> None: ...
def glStencilMaskSeparate(face: Incomplete, mask: Incomplete) -> None: ...
def glStencilOp(fail: Incomplete, zfail: Incomplete, zpass: Incomplete) -> None: ...
def glStencilOpSeparate(face: Incomplete, sfail: Incomplete, dpfail: Incomplete, dppass: Incomplete) -> None: ...
def glTexImage2D(
    target: Incomplete,
    level: Incomplete,
    internalformat: Incomplete,
    width: Incomplete,
    height: Incomplete,
    border: Incomplete,
    format: Incomplete,
    type: Incomplete,
    pixels: Incomplete,
) -> None: ...
def glTexImage3D(
    target: Incomplete,
    level: Incomplete,
    internalformat: Incomplete,
    width: Incomplete,
    height: Incomplete,
    depth: Incomplete,
    border: Incomplete,
    format: Incomplete,
    type: Incomplete,
    pixels: Incomplete,
) -> None: ...
def glTexParameterf(target: Incomplete, pname: Incomplete, param: Incomplete) -> None: ...
def glTexParameterfv(target: Incomplete, pname: Incomplete, params: Incomplete) -> None: ...
def glTexParameteri(target: Incomplete, pname: Incomplete, param: Incomplete) -> None: ...
def glTexParameteriv(target: Incomplete, pname: Incomplete, params: Incomplete) -> None: ...
def glTexSubImage2D(
    target: Incomplete,
    level: Incomplete,
    xoffset: Incomplete,
    yoffset: Incomplete,
    width: Incomplete,
    height: Incomplete,
    format: Incomplete,
    type: Incomplete,
    pixels: Incomplete,
) -> None: ...
def glTexSubImage3D(
    target: Incomplete,
    level: Incomplete,
    xoffset: Incomplete,
    yoffset: Incomplete,
    zoffset: Incomplete,
    width: Incomplete,
    height: Incomplete,
    depth: Incomplete,
    format: Incomplete,
    type: Incomplete,
    pixels: Incomplete,
) -> None: ...
def glTransformFeedbackVaryings(
    program: Incomplete, count: Incomplete, varyings: Incomplete, bufferMode: Incomplete
) -> None: ...
def glUniform1f(location: Incomplete, v0: Incomplete) -> None: ...
def glUniform1fv(location: Incomplete, count: Incomplete, value: Incomplete) -> None: ...
def glUniform1i(location: Incomplete, v0: Incomplete) -> None: ...
def glUniform1iv(location: Incomplete, count: Incomplete, value: Incomplete) -> None: ...
def glUniform1ui(location: Incomplete, v0: Incomplete) -> None: ...
def glUniform1uiv(location: Incomplete, count: Incomplete, value: Incomplete) -> None: ...
def glUniform2f(location: Incomplete, v0: Incomplete, v1: Incomplete) -> None: ...
def glUniform2fv(location: Incomplete, count: Incomplete, value: Incomplete) -> None: ...
def glUniform2i(location: Incomplete, v0: Incomplete, v1: Incomplete) -> None: ...
def glUniform2iv(location: Incomplete, count: Incomplete, value: Incomplete) -> None: ...
def glUniform2ui(location: Incomplete, v0: Incomplete, v1: Incomplete) -> None: ...
def glUniform2uiv(location: Incomplete, count: Incomplete, value: Incomplete) -> None: ...
def glUniform3f(location: Incomplete, v0: Incomplete, v1: Incomplete, v2: Incomplete) -> None: ...
def glUniform3fv(location: Incomplete, count: Incomplete, value: Incomplete) -> None: ...
def glUniform3i(location: Incomplete, v0: Incomplete, v1: Incomplete, v2: Incomplete) -> None: ...
def glUniform3iv(location: Incomplete, count: Incomplete, value: Incomplete) -> None: ...
def glUniform3ui(location: Incomplete, v0: Incomplete, v1: Incomplete, v2: Incomplete) -> None: ...
def glUniform3uiv(location: Incomplete, count: Incomplete, value: Incomplete) -> None: ...
def glUniform4f(location: Incomplete, v0: Incomplete, v1: Incomplete, v2: Incomplete, v3: Incomplete) -> None: ...
def glUniform4fv(location: Incomplete, count: Incomplete, value: Incomplete) -> None: ...
def glUniform4i(location: Incomplete, v0: Incomplete, v1: Incomplete, v2: Incomplete, v3: Incomplete) -> None: ...
def glUniform4iv(location: Incomplete, count: Incomplete, value: Incomplete) -> None: ...
def glUniform4ui(location: Incomplete, v0: Incomplete, v1: Incomplete, v2: Incomplete, v3: Incomplete) -> None: ...
def glUniform4uiv(location: Incomplete, count: Incomplete, value: Incomplete) -> None: ...
def glUniformMatrix2fv(location: Incomplete, count: Incomplete, transpose: Incomplete, value: Incomplete) -> None: ...
def glUniformMatrix2x3fv(location: Incomplete, count: Incomplete, transpose: Incomplete, value: Incomplete) -> None: ...
def glUniformMatrix2x4fv(location: Incomplete, count: Incomplete, transpose: Incomplete, value: Incomplete) -> None: ...
def glUniformMatrix3fv(location: Incomplete, count: Incomplete, transpose: Incomplete, value: Incomplete) -> None: ...
def glUniformMatrix3x2fv(location: Incomplete, count: Incomplete, transpose: Incomplete, value: Incomplete) -> None: ...
def glUniformMatrix3x4fv(location: Incomplete, count: Incomplete, transpose: Incomplete, value: Incomplete) -> None: ...
def glUniformMatrix4fv(location: Incomplete, count: Incomplete, transpose: Incomplete, value: Incomplete) -> None: ...
def glUniformMatrix4x2fv(location: Incomplete, count: Incomplete, transpose: Incomplete, value: Incomplete) -> None: ...
def glUniformMatrix4x3fv(location: Incomplete, count: Incomplete, transpose: Incomplete, value: Incomplete) -> None: ...
def glUnmapBuffer(target: Incomplete) -> None: ...
def glUseProgram(program: Incomplete) -> None: ...
def glValidateProgram(program: Incomplete) -> None: ...
def glVertexAttrib1f(index: Incomplete, x: Incomplete) -> None: ...
def glVertexAttrib1fv(index: Incomplete, v: Incomplete) -> None: ...
def glVertexAttrib2f(index: Incomplete, x: Incomplete, y: Incomplete) -> None: ...
def glVertexAttrib2fv(index: Incomplete, v: Incomplete) -> None: ...
def glVertexAttrib3f(index: Incomplete, x: Incomplete, y: Incomplete, z: Incomplete) -> None: ...
def glVertexAttrib3fv(index: Incomplete, v: Incomplete) -> None: ...
def glVertexAttrib4f(index: Incomplete, x: Incomplete, y: Incomplete, z: Incomplete, w: Incomplete) -> None: ...
def glVertexAttrib4fv(index: Incomplete, v: Incomplete) -> None: ...
def glVertexAttribI4i(index: Incomplete, x: Incomplete, y: Incomplete, z: Incomplete, w: Incomplete) -> None: ...
def glVertexAttribI4iv(index: Incomplete, v: Incomplete) -> None: ...
def glVertexAttribI4ui(index: Incomplete, x: Incomplete, y: Incomplete, z: Incomplete, w: Incomplete) -> None: ...
def glVertexAttribI4uiv(index: Incomplete, v: Incomplete) -> None: ...
def glVertexAttribIPointer(
    index: Incomplete, size: Incomplete, type: Incomplete, stride: Incomplete, pointer: Incomplete
) -> None: ...
def glVertexAttribPointer(
    index: Incomplete,
    size: Incomplete,
    type: Incomplete,
    normalized: Incomplete,
    stride: Incomplete,
    pointer: Incomplete,
) -> None: ...
def glViewport(x: Incomplete, y: Incomplete, width: Incomplete, height: Incomplete) -> None: ...

class ptr:
    def __init__(self, /, *args, **kwargs) -> None: ...
    def __reduce__(self) -> None: ...

GL_ACTIVE_ATTRIBUTES: int
GL_ACTIVE_ATTRIBUTE_MAX_LENGTH: int
GL_ACTIVE_TEXTURE: int
GL_ACTIVE_UNIFORMS: int
GL_ACTIVE_UNIFORM_MAX_LENGTH: int
GL_ALIASED_LINE_WIDTH_RANGE: int
GL_ALIASED_POINT_SIZE_RANGE: int
GL_ALPHA: int
GL_ALPHA_BITS: int
GL_ALWAYS: int
GL_ARRAY_BUFFER: int
GL_ARRAY_BUFFER_BINDING: int
GL_ATTACHED_SHADERS: int
GL_BACK: int
GL_BLEND: int
GL_BLEND_COLOR: int
GL_BLEND_DST_ALPHA: int
GL_BLEND_DST_RGB: int
GL_BLEND_EQUATION: int
GL_BLEND_EQUATION_ALPHA: int
GL_BLEND_EQUATION_RGB: int
GL_BLEND_SRC_ALPHA: int
GL_BLEND_SRC_RGB: int
GL_BLUE: int
GL_BLUE_BITS: int
GL_BOOL: int
GL_BOOL_VEC2: int
GL_BOOL_VEC3: int
GL_BOOL_VEC4: int
GL_BUFFER_ACCESS_FLAGS: int
GL_BUFFER_MAPPED: int
GL_BUFFER_MAP_LENGTH: int
GL_BUFFER_MAP_OFFSET: int
GL_BUFFER_MAP_POINTER: int
GL_BUFFER_SIZE: int
GL_BUFFER_USAGE: int
GL_BYTE: int
GL_CCW: int
GL_CLAMP_TO_EDGE: int
GL_COLOR: int
GL_COLOR_ATTACHMENT0: int
GL_COLOR_ATTACHMENT1: int
GL_COLOR_ATTACHMENT10: int
GL_COLOR_ATTACHMENT11: int
GL_COLOR_ATTACHMENT12: int
GL_COLOR_ATTACHMENT13: int
GL_COLOR_ATTACHMENT14: int
GL_COLOR_ATTACHMENT15: int
GL_COLOR_ATTACHMENT16: int
GL_COLOR_ATTACHMENT17: int
GL_COLOR_ATTACHMENT18: int
GL_COLOR_ATTACHMENT19: int
GL_COLOR_ATTACHMENT2: int
GL_COLOR_ATTACHMENT20: int
GL_COLOR_ATTACHMENT21: int
GL_COLOR_ATTACHMENT22: int
GL_COLOR_ATTACHMENT23: int
GL_COLOR_ATTACHMENT24: int
GL_COLOR_ATTACHMENT25: int
GL_COLOR_ATTACHMENT26: int
GL_COLOR_ATTACHMENT27: int
GL_COLOR_ATTACHMENT28: int
GL_COLOR_ATTACHMENT29: int
GL_COLOR_ATTACHMENT3: int
GL_COLOR_ATTACHMENT30: int
GL_COLOR_ATTACHMENT31: int
GL_COLOR_ATTACHMENT4: int
GL_COLOR_ATTACHMENT5: int
GL_COLOR_ATTACHMENT6: int
GL_COLOR_ATTACHMENT7: int
GL_COLOR_ATTACHMENT8: int
GL_COLOR_ATTACHMENT9: int
GL_COLOR_BUFFER_BIT: int
GL_COLOR_CLEAR_VALUE: int
GL_COLOR_WRITEMASK: int
GL_COMPARE_REF_TO_TEXTURE: int
GL_COMPILE_STATUS: int
GL_COMPRESSED_TEXTURE_FORMATS: int
GL_CONSTANT_ALPHA: int
GL_CONSTANT_COLOR: int
GL_CULL_FACE: int
GL_CULL_FACE_MODE: int
GL_CURRENT_PROGRAM: int
GL_CURRENT_QUERY: int
GL_CURRENT_VERTEX_ATTRIB: int
GL_CW: int
GL_DECR: int
GL_DECR_WRAP: int
GL_DELETE_STATUS: int
GL_DEPTH: int
GL_DEPTH24_STENCIL8: int
GL_DEPTH32F_STENCIL8: int
GL_DEPTH_ATTACHMENT: int
GL_DEPTH_BITS: int
GL_DEPTH_BUFFER_BIT: int
GL_DEPTH_CLEAR_VALUE: int
GL_DEPTH_COMPONENT: int
GL_DEPTH_COMPONENT16: int
GL_DEPTH_COMPONENT24: int
GL_DEPTH_COMPONENT32F: int
GL_DEPTH_FUNC: int
GL_DEPTH_RANGE: int
GL_DEPTH_STENCIL: int
GL_DEPTH_STENCIL_ATTACHMENT: int
GL_DEPTH_TEST: int
GL_DEPTH_WRITEMASK: int
GL_DITHER: int
GL_DONT_CARE: int
GL_DRAW_BUFFER0: int
GL_DRAW_BUFFER1: int
GL_DRAW_BUFFER10: int
GL_DRAW_BUFFER11: int
GL_DRAW_BUFFER12: int
GL_DRAW_BUFFER13: int
GL_DRAW_BUFFER14: int
GL_DRAW_BUFFER15: int
GL_DRAW_BUFFER2: int
GL_DRAW_BUFFER3: int
GL_DRAW_BUFFER4: int
GL_DRAW_BUFFER5: int
GL_DRAW_BUFFER6: int
GL_DRAW_BUFFER7: int
GL_DRAW_BUFFER8: int
GL_DRAW_BUFFER9: int
GL_DRAW_FRAMEBUFFER: int
GL_DRAW_FRAMEBUFFER_BINDING: int
GL_DST_ALPHA: int
GL_DST_COLOR: int
GL_DYNAMIC_COPY: int
GL_DYNAMIC_DRAW: int
GL_DYNAMIC_READ: int
GL_ELEMENT_ARRAY_BUFFER: int
GL_ELEMENT_ARRAY_BUFFER_BINDING: int
GL_EQUAL: int
GL_EXTENSIONS: int
GL_FALSE: int
GL_FASTEST: int
GL_FLOAT: int
GL_FLOAT_32_UNSIGNED_INT_24_8_REV: int
GL_FLOAT_MAT2: int
GL_FLOAT_MAT2x3: int
GL_FLOAT_MAT2x4: int
GL_FLOAT_MAT3: int
GL_FLOAT_MAT3x2: int
GL_FLOAT_MAT3x4: int
GL_FLOAT_MAT4: int
GL_FLOAT_MAT4x2: int
GL_FLOAT_MAT4x3: int
GL_FLOAT_VEC2: int
GL_FLOAT_VEC3: int
GL_FLOAT_VEC4: int
GL_FRAGMENT_SHADER: int
GL_FRAGMENT_SHADER_DERIVATIVE_HINT: int
GL_FRAMEBUFFER: int
GL_FRAMEBUFFER_ATTACHMENT_ALPHA_SIZE: int
GL_FRAMEBUFFER_ATTACHMENT_BLUE_SIZE: int
GL_FRAMEBUFFER_ATTACHMENT_COLOR_ENCODING: int
GL_FRAMEBUFFER_ATTACHMENT_COMPONENT_TYPE: int
GL_FRAMEBUFFER_ATTACHMENT_DEPTH_SIZE: int
GL_FRAMEBUFFER_ATTACHMENT_GREEN_SIZE: int
GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME: int
GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE: int
GL_FRAMEBUFFER_ATTACHMENT_RED_SIZE: int
GL_FRAMEBUFFER_ATTACHMENT_STENCIL_SIZE: int
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE: int
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LAYER: int
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL: int
GL_FRAMEBUFFER_BINDING: int
GL_FRAMEBUFFER_COMPLETE: int
GL_FRAMEBUFFER_DEFAULT: int
GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT: int
GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT: int
GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE: int
GL_FRAMEBUFFER_UNDEFINED: int
GL_FRAMEBUFFER_UNSUPPORTED: int
GL_FRONT: int
GL_FRONT_AND_BACK: int
GL_FRONT_FACE: int
GL_FUNC_ADD: int
GL_FUNC_REVERSE_SUBTRACT: int
GL_FUNC_SUBTRACT: int
GL_GENERATE_MIPMAP_HINT: int
GL_GEQUAL: int
GL_GREATER: int
GL_GREEN: int
GL_GREEN_BITS: int
GL_HALF_FLOAT: int
GL_INCR: int
GL_INCR_WRAP: int
GL_INFO_LOG_LENGTH: int
GL_INT: int
GL_INTERLEAVED_ATTRIBS: int
GL_INT_SAMPLER_2D: int
GL_INT_SAMPLER_2D_ARRAY: int
GL_INT_SAMPLER_3D: int
GL_INT_SAMPLER_CUBE: int
GL_INT_VEC2: int
GL_INT_VEC3: int
GL_INT_VEC4: int
GL_INVALID_ENUM: int
GL_INVALID_FRAMEBUFFER_OPERATION: int
GL_INVALID_OPERATION: int
GL_INVALID_VALUE: int
GL_INVERT: int
GL_KEEP: int
GL_LEQUAL: int
GL_LESS: int
GL_LINEAR: int
GL_LINEAR_MIPMAP_LINEAR: int
GL_LINEAR_MIPMAP_NEAREST: int
GL_LINES: int
GL_LINE_LOOP: int
GL_LINE_STRIP: int
GL_LINE_WIDTH: int
GL_LINK_STATUS: int
GL_LUMINANCE: int
GL_LUMINANCE_ALPHA: int
GL_MAJOR_VERSION: int
GL_MAP_FLUSH_EXPLICIT_BIT: int
GL_MAP_INVALIDATE_BUFFER_BIT: int
GL_MAP_INVALIDATE_RANGE_BIT: int
GL_MAP_READ_BIT: int
GL_MAP_UNSYNCHRONIZED_BIT: int
GL_MAP_WRITE_BIT: int
GL_MAX: int
GL_MAX_3D_TEXTURE_SIZE: int
GL_MAX_ARRAY_TEXTURE_LAYERS: int
GL_MAX_COLOR_ATTACHMENTS: int
GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS: int
GL_MAX_CUBE_MAP_TEXTURE_SIZE: int
GL_MAX_DRAW_BUFFERS: int
GL_MAX_ELEMENTS_INDICES: int
GL_MAX_ELEMENTS_VERTICES: int
GL_MAX_FRAGMENT_UNIFORM_COMPONENTS: int
GL_MAX_PROGRAM_TEXEL_OFFSET: int
GL_MAX_RENDERBUFFER_SIZE: int
GL_MAX_SAMPLES: int
GL_MAX_TEXTURE_IMAGE_UNITS: int
GL_MAX_TEXTURE_LOD_BIAS: int
GL_MAX_TEXTURE_SIZE: int
GL_MAX_TRANSFORM_FEEDBACK_INTERLEAVED_COMPONENTS: int
GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_ATTRIBS: int
GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_COMPONENTS: int
GL_MAX_VARYING_COMPONENTS: int
GL_MAX_VERTEX_ATTRIBS: int
GL_MAX_VERTEX_TEXTURE_IMAGE_UNITS: int
GL_MAX_VERTEX_UNIFORM_COMPONENTS: int
GL_MAX_VIEWPORT_DIMS: int
GL_MIN: int
GL_MINOR_VERSION: int
GL_MIN_PROGRAM_TEXEL_OFFSET: int
GL_MIRRORED_REPEAT: int
GL_NEAREST: int
GL_NEAREST_MIPMAP_LINEAR: int
GL_NEAREST_MIPMAP_NEAREST: int
GL_NEVER: int
GL_NICEST: int
GL_NONE: int
GL_NOTEQUAL: int
GL_NO_ERROR: int
GL_NUM_COMPRESSED_TEXTURE_FORMATS: int
GL_NUM_EXTENSIONS: int
GL_ONE: int
GL_ONE_MINUS_CONSTANT_ALPHA: int
GL_ONE_MINUS_CONSTANT_COLOR: int
GL_ONE_MINUS_DST_ALPHA: int
GL_ONE_MINUS_DST_COLOR: int
GL_ONE_MINUS_SRC_ALPHA: int
GL_ONE_MINUS_SRC_COLOR: int
GL_OUT_OF_MEMORY: int
GL_PACK_ALIGNMENT: int
GL_PACK_ROW_LENGTH: int
GL_PACK_SKIP_PIXELS: int
GL_PACK_SKIP_ROWS: int
GL_PIXEL_PACK_BUFFER: int
GL_PIXEL_PACK_BUFFER_BINDING: int
GL_PIXEL_UNPACK_BUFFER: int
GL_PIXEL_UNPACK_BUFFER_BINDING: int
GL_POINTS: int
GL_POLYGON_OFFSET_FACTOR: int
GL_POLYGON_OFFSET_FILL: int
GL_POLYGON_OFFSET_UNITS: int
GL_QUERY_RESULT: int
GL_QUERY_RESULT_AVAILABLE: int
GL_R11F_G11F_B10F: int
GL_R16F: int
GL_R16I: int
GL_R16UI: int
GL_R32F: int
GL_R32I: int
GL_R32UI: int
GL_R8: int
GL_R8I: int
GL_R8UI: int
GL_RASTERIZER_DISCARD: int
GL_READ_BUFFER: int
GL_READ_FRAMEBUFFER: int
GL_READ_FRAMEBUFFER_BINDING: int
GL_RED: int
GL_RED_BITS: int
GL_RED_INTEGER: int
GL_RENDERBUFFER: int
GL_RENDERBUFFER_ALPHA_SIZE: int
GL_RENDERBUFFER_BINDING: int
GL_RENDERBUFFER_BLUE_SIZE: int
GL_RENDERBUFFER_DEPTH_SIZE: int
GL_RENDERBUFFER_GREEN_SIZE: int
GL_RENDERBUFFER_HEIGHT: int
GL_RENDERBUFFER_INTERNAL_FORMAT: int
GL_RENDERBUFFER_RED_SIZE: int
GL_RENDERBUFFER_SAMPLES: int
GL_RENDERBUFFER_STENCIL_SIZE: int
GL_RENDERBUFFER_WIDTH: int
GL_RENDERER: int
GL_REPEAT: int
GL_REPLACE: int
GL_RG: int
GL_RG16F: int
GL_RG16I: int
GL_RG16UI: int
GL_RG32F: int
GL_RG32I: int
GL_RG32UI: int
GL_RG8: int
GL_RG8I: int
GL_RG8UI: int
GL_RGB: int
GL_RGB10_A2: int
GL_RGB16F: int
GL_RGB16I: int
GL_RGB16UI: int
GL_RGB32F: int
GL_RGB32I: int
GL_RGB32UI: int
GL_RGB5_A1: int
GL_RGB8: int
GL_RGB8I: int
GL_RGB8UI: int
GL_RGB9_E5: int
GL_RGBA: int
GL_RGBA16F: int
GL_RGBA16I: int
GL_RGBA16UI: int
GL_RGBA32F: int
GL_RGBA32I: int
GL_RGBA32UI: int
GL_RGBA4: int
GL_RGBA8: int
GL_RGBA8I: int
GL_RGBA8UI: int
GL_RGBA_INTEGER: int
GL_RGB_INTEGER: int
GL_RG_INTEGER: int
GL_SAMPLER_2D: int
GL_SAMPLER_2D_ARRAY: int
GL_SAMPLER_2D_ARRAY_SHADOW: int
GL_SAMPLER_2D_SHADOW: int
GL_SAMPLER_3D: int
GL_SAMPLER_CUBE: int
GL_SAMPLER_CUBE_SHADOW: int
GL_SAMPLES: int
GL_SAMPLE_ALPHA_TO_COVERAGE: int
GL_SAMPLE_BUFFERS: int
GL_SAMPLE_COVERAGE: int
GL_SAMPLE_COVERAGE_INVERT: int
GL_SAMPLE_COVERAGE_VALUE: int
GL_SCISSOR_BOX: int
GL_SCISSOR_TEST: int
GL_SEPARATE_ATTRIBS: int
GL_SHADER_SOURCE_LENGTH: int
GL_SHADER_TYPE: int
GL_SHADING_LANGUAGE_VERSION: int
GL_SHORT: int
GL_SRC_ALPHA: int
GL_SRC_ALPHA_SATURATE: int
GL_SRC_COLOR: int
GL_SRGB: int
GL_SRGB8: int
GL_SRGB8_ALPHA8: int
GL_STATIC_COPY: int
GL_STATIC_DRAW: int
GL_STATIC_READ: int
GL_STENCIL: int
GL_STENCIL_ATTACHMENT: int
GL_STENCIL_BACK_FAIL: int
GL_STENCIL_BACK_FUNC: int
GL_STENCIL_BACK_PASS_DEPTH_FAIL: int
GL_STENCIL_BACK_PASS_DEPTH_PASS: int
GL_STENCIL_BACK_REF: int
GL_STENCIL_BACK_VALUE_MASK: int
GL_STENCIL_BACK_WRITEMASK: int
GL_STENCIL_BITS: int
GL_STENCIL_BUFFER_BIT: int
GL_STENCIL_CLEAR_VALUE: int
GL_STENCIL_FAIL: int
GL_STENCIL_FUNC: int
GL_STENCIL_INDEX8: int
GL_STENCIL_PASS_DEPTH_FAIL: int
GL_STENCIL_PASS_DEPTH_PASS: int
GL_STENCIL_REF: int
GL_STENCIL_TEST: int
GL_STENCIL_VALUE_MASK: int
GL_STENCIL_WRITEMASK: int
GL_STREAM_COPY: int
GL_STREAM_DRAW: int
GL_STREAM_READ: int
GL_SUBPIXEL_BITS: int
GL_TEXTURE: int
GL_TEXTURE0: int
GL_TEXTURE1: int
GL_TEXTURE10: int
GL_TEXTURE11: int
GL_TEXTURE12: int
GL_TEXTURE13: int
GL_TEXTURE14: int
GL_TEXTURE15: int
GL_TEXTURE16: int
GL_TEXTURE17: int
GL_TEXTURE18: int
GL_TEXTURE19: int
GL_TEXTURE2: int
GL_TEXTURE20: int
GL_TEXTURE21: int
GL_TEXTURE22: int
GL_TEXTURE23: int
GL_TEXTURE24: int
GL_TEXTURE25: int
GL_TEXTURE26: int
GL_TEXTURE27: int
GL_TEXTURE28: int
GL_TEXTURE29: int
GL_TEXTURE3: int
GL_TEXTURE30: int
GL_TEXTURE31: int
GL_TEXTURE4: int
GL_TEXTURE5: int
GL_TEXTURE6: int
GL_TEXTURE7: int
GL_TEXTURE8: int
GL_TEXTURE9: int
GL_TEXTURE_2D: int
GL_TEXTURE_2D_ARRAY: int
GL_TEXTURE_3D: int
GL_TEXTURE_BASE_LEVEL: int
GL_TEXTURE_BINDING_2D: int
GL_TEXTURE_BINDING_2D_ARRAY: int
GL_TEXTURE_BINDING_3D: int
GL_TEXTURE_BINDING_CUBE_MAP: int
GL_TEXTURE_COMPARE_FUNC: int
GL_TEXTURE_COMPARE_MODE: int
GL_TEXTURE_CUBE_MAP: int
GL_TEXTURE_CUBE_MAP_NEGATIVE_X: int
GL_TEXTURE_CUBE_MAP_NEGATIVE_Y: int
GL_TEXTURE_CUBE_MAP_NEGATIVE_Z: int
GL_TEXTURE_CUBE_MAP_POSITIVE_X: int
GL_TEXTURE_CUBE_MAP_POSITIVE_Y: int
GL_TEXTURE_CUBE_MAP_POSITIVE_Z: int
GL_TEXTURE_MAG_FILTER: int
GL_TEXTURE_MAX_LEVEL: int
GL_TEXTURE_MAX_LOD: int
GL_TEXTURE_MIN_FILTER: int
GL_TEXTURE_MIN_LOD: int
GL_TEXTURE_WRAP_R: int
GL_TEXTURE_WRAP_S: int
GL_TEXTURE_WRAP_T: int
GL_TRANSFORM_FEEDBACK_BUFFER: int
GL_TRANSFORM_FEEDBACK_BUFFER_BINDING: int
GL_TRANSFORM_FEEDBACK_BUFFER_MODE: int
GL_TRANSFORM_FEEDBACK_BUFFER_SIZE: int
GL_TRANSFORM_FEEDBACK_BUFFER_START: int
GL_TRANSFORM_FEEDBACK_PRIMITIVES_WRITTEN: int
GL_TRANSFORM_FEEDBACK_VARYINGS: int
GL_TRANSFORM_FEEDBACK_VARYING_MAX_LENGTH: int
GL_TRIANGLES: int
GL_TRIANGLE_FAN: int
GL_TRIANGLE_STRIP: int
GL_TRUE: int
GL_UNPACK_ALIGNMENT: int
GL_UNPACK_IMAGE_HEIGHT: int
GL_UNPACK_ROW_LENGTH: int
GL_UNPACK_SKIP_IMAGES: int
GL_UNPACK_SKIP_PIXELS: int
GL_UNPACK_SKIP_ROWS: int
GL_UNSIGNED_BYTE: int
GL_UNSIGNED_INT: int
GL_UNSIGNED_INT_10F_11F_11F_REV: int
GL_UNSIGNED_INT_24_8: int
GL_UNSIGNED_INT_2_10_10_10_REV: int
GL_UNSIGNED_INT_5_9_9_9_REV: int
GL_UNSIGNED_INT_SAMPLER_2D: int
GL_UNSIGNED_INT_SAMPLER_2D_ARRAY: int
GL_UNSIGNED_INT_SAMPLER_3D: int
GL_UNSIGNED_INT_SAMPLER_CUBE: int
GL_UNSIGNED_INT_VEC2: int
GL_UNSIGNED_INT_VEC3: int
GL_UNSIGNED_INT_VEC4: int
GL_UNSIGNED_NORMALIZED: int
GL_UNSIGNED_SHORT: int
GL_UNSIGNED_SHORT_4_4_4_4: int
GL_UNSIGNED_SHORT_5_5_5_1: int
GL_UNSIGNED_SHORT_5_6_5: int
GL_VALIDATE_STATUS: int
GL_VENDOR: int
GL_VERSION: int
GL_VERTEX_ARRAY_BINDING: int
GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING: int
GL_VERTEX_ATTRIB_ARRAY_ENABLED: int
GL_VERTEX_ATTRIB_ARRAY_INTEGER: int
GL_VERTEX_ATTRIB_ARRAY_NORMALIZED: int
GL_VERTEX_ATTRIB_ARRAY_POINTER: int
GL_VERTEX_ATTRIB_ARRAY_SIZE: int
GL_VERTEX_ATTRIB_ARRAY_STRIDE: int
GL_VERTEX_ATTRIB_ARRAY_TYPE: int
GL_VERTEX_SHADER: int
GL_VIEWPORT: int
GL_ZERO: int
