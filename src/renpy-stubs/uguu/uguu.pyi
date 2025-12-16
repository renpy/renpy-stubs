from _frozen_importlib import BuiltinImporter as BuiltinImporter

class Buffer:
    def __buffer__(self, flags) -> None: ...
    def __reduce__(self) -> None: ...
    def __release_buffer__(self, buffer) -> None: ...

class BytesBuffer(Buffer):
    def __init__(self, /, *args, **kwargs) -> None: ...
    def __reduce__(self) -> None: ...
    def get(self) -> None: ...

class BytesListBuffer(Buffer):
    def __init__(self, /, *args, **kwargs) -> None: ...
    def __reduce__(self) -> None: ...

class FloatBuffer(Buffer):
    def __init__(self, /, *args, **kwargs) -> None: ...
    def __getitem__(self, key) -> None: ...
    def __reduce__(self) -> None: ...

class IntBuffer(Buffer):
    def __init__(self, /, *args, **kwargs) -> None: ...
    def __getitem__(self, key) -> None: ...
    def __reduce__(self) -> None: ...

def glActiveTexture(texture) -> None: ...
def glAttachShader(program, shader) -> None: ...
def glBeginQuery(target, id) -> None: ...
def glBeginTransformFeedback(primitiveMode) -> None: ...
def glBindAttribLocation(program, index, name) -> None: ...
def glBindBuffer(target, buffer) -> None: ...
def glBindBufferBase(target, index, buffer) -> None: ...
def glBindBufferRange(target, index, buffer, offset, size) -> None: ...
def glBindFramebuffer(target, framebuffer) -> None: ...
def glBindRenderbuffer(target, renderbuffer) -> None: ...
def glBindTexture(target, texture) -> None: ...
def glBindVertexArray(array) -> None: ...
def glBlendColor(red, green, blue, alpha) -> None: ...
def glBlendEquation(mode) -> None: ...
def glBlendEquationSeparate(modeRGB, modeAlpha) -> None: ...
def glBlendFunc(sfactor, dfactor) -> None: ...
def glBlendFuncSeparate(sfactorRGB, dfactorRGB, sfactorAlpha, dfactorAlpha) -> None: ...
def glBlitFramebuffer(srcX0, srcY0, srcX1, srcY1, dstX0, dstY0, dstX1, dstY1, mask, filter) -> None: ...
def glBufferData(target, size, data, usage) -> None: ...
def glBufferSubData(target, offset, size, data) -> None: ...
def glCheckFramebufferStatus(target) -> None: ...
def glClear(mask) -> None: ...
def glClearBufferfi(buffer, drawbuffer, depth, stencil) -> None: ...
def glClearBufferfv(buffer, drawbuffer, value) -> None: ...
def glClearBufferiv(buffer, drawbuffer, value) -> None: ...
def glClearBufferuiv(buffer, drawbuffer, value) -> None: ...
def glClearColor(red, green, blue, alpha) -> None: ...
def glClearStencil(s) -> None: ...
def glColorMask(red, green, blue, alpha) -> None: ...
def glCompileShader(shader) -> None: ...
def glCompressedTexImage2D(target, level, internalformat, width, height, border, imageSize, data) -> None: ...
def glCompressedTexImage3D(target, level, internalformat, width, height, depth, border, imageSize, data) -> None: ...
def glCompressedTexSubImage2D(target, level, xoffset, yoffset, width, height, format, imageSize, data) -> None: ...
def glCompressedTexSubImage3D(
    target, level, xoffset, yoffset, zoffset, width, height, depth, format, imageSize, data
) -> None: ...
def glCopyTexImage2D(target, level, internalformat, x, y, width, height, border) -> None: ...
def glCopyTexSubImage2D(target, level, xoffset, yoffset, x, y, width, height) -> None: ...
def glCopyTexSubImage3D(target, level, xoffset, yoffset, zoffset, x, y, width, height) -> None: ...
def glCreateProgram() -> None: ...
def glCreateShader(type) -> None: ...
def glCullFace(mode) -> None: ...
def glDeleteBuffers(n, buffers) -> None: ...
def glDeleteFramebuffers(n, framebuffers) -> None: ...
def glDeleteProgram(program) -> None: ...
def glDeleteQueries(n, ids) -> None: ...
def glDeleteRenderbuffers(n, renderbuffers) -> None: ...
def glDeleteShader(shader) -> None: ...
def glDeleteTextures(n, textures) -> None: ...
def glDeleteVertexArrays(n, arrays) -> None: ...
def glDepthFunc(func) -> None: ...
def glDepthMask(flag) -> None: ...
def glDetachShader(program, shader) -> None: ...
def glDisable(cap) -> None: ...
def glDisableVertexAttribArray(index) -> None: ...
def glDrawArrays(mode, first, count) -> None: ...
def glDrawBuffers(n, bufs) -> None: ...
def glDrawElements(mode, count, type, indices) -> None: ...
def glDrawRangeElements(mode, start, end, count, type, indices) -> None: ...
def glEnable(cap) -> None: ...
def glEnableVertexAttribArray(index) -> None: ...
def glEndQuery(target) -> None: ...
def glEndTransformFeedback() -> None: ...
def glFinish() -> None: ...
def glFlush() -> None: ...
def glFlushMappedBufferRange(target, offset, length) -> None: ...
def glFramebufferRenderbuffer(target, attachment, renderbuffertarget, renderbuffer) -> None: ...
def glFramebufferTexture2D(target, attachment, textarget, texture, level) -> None: ...
def glFramebufferTextureLayer(target, attachment, texture, level, layer) -> None: ...
def glFrontFace(mode) -> None: ...
def glGenBuffers(n, buffers) -> None: ...
def glGenFramebuffers(n, framebuffers) -> None: ...
def glGenQueries(n, ids) -> None: ...
def glGenRenderbuffers(n, renderbuffers) -> None: ...
def glGenTextures(n, textures) -> None: ...
def glGenVertexArrays(n, arrays) -> None: ...
def glGenerateMipmap(target) -> None: ...
def glGetActiveAttrib(program, index, bufSize, length, size, type, name) -> None: ...
def glGetActiveUniform(program, index, bufSize, length, size, type, name) -> None: ...
def glGetAttachedShaders(program, maxCount, count, shaders) -> None: ...
def glGetAttribLocation(program, name) -> None: ...
def glGetBooleanv(pname, data) -> None: ...
def glGetBufferParameteriv(target, pname, params) -> None: ...
def glGetBufferPointerv(target, pname, params) -> None: ...
def glGetError() -> None: ...
def glGetFloatv(pname, data) -> None: ...
def glGetFragDataLocation(program, name) -> None: ...
def glGetFramebufferAttachmentParameteriv(target, attachment, pname, params) -> None: ...
def glGetIntegeri_v(target, index, data) -> None: ...
def glGetIntegerv(pname, data) -> None: ...
def glGetProgramInfoLog(program, bufSize, length, infoLog) -> None: ...
def glGetProgramiv(program, pname, params) -> None: ...
def glGetQueryObjectuiv(id, pname, params) -> None: ...
def glGetQueryiv(target, pname, params) -> None: ...
def glGetRenderbufferParameteriv(target, pname, params) -> None: ...
def glGetShaderInfoLog(shader, bufSize, length, infoLog) -> None: ...
def glGetShaderSource(shader, bufSize, length, source) -> None: ...
def glGetShaderiv(shader, pname, params) -> None: ...
def glGetString(name) -> None: ...
def glGetStringi(name, index) -> None: ...
def glGetTexParameterfv(target, pname, params) -> None: ...
def glGetTexParameteriv(target, pname, params) -> None: ...
def glGetTransformFeedbackVarying(program, index, bufSize, length, size, type, name) -> None: ...
def glGetUniformLocation(program, name) -> None: ...
def glGetUniformfv(program, location, params) -> None: ...
def glGetUniformiv(program, location, params) -> None: ...
def glGetUniformuiv(program, location, params) -> None: ...
def glGetVertexAttribIiv(index, pname, params) -> None: ...
def glGetVertexAttribIuiv(index, pname, params) -> None: ...
def glGetVertexAttribPointerv(index, pname, pointer) -> None: ...
def glGetVertexAttribfv(index, pname, params) -> None: ...
def glGetVertexAttribiv(index, pname, params) -> None: ...
def glHint(target, mode) -> None: ...
def glIsBuffer(buffer) -> None: ...
def glIsEnabled(cap) -> None: ...
def glIsFramebuffer(framebuffer) -> None: ...
def glIsProgram(program) -> None: ...
def glIsQuery(id) -> None: ...
def glIsRenderbuffer(renderbuffer) -> None: ...
def glIsShader(shader) -> None: ...
def glIsTexture(texture) -> None: ...
def glIsVertexArray(array) -> None: ...
def glLineWidth(width) -> None: ...
def glLinkProgram(program) -> None: ...
def glPixelStorei(pname, param) -> None: ...
def glPolygonOffset(factor, units) -> None: ...
def glReadBuffer(src) -> None: ...
def glReadPixels(x, y, width, height, format, type, pixels) -> None: ...
def glRenderbufferStorage(target, internalformat, width, height) -> None: ...
def glRenderbufferStorageMultisample(target, samples, internalformat, width, height) -> None: ...
def glSampleCoverage(value, invert) -> None: ...
def glScissor(x, y, width, height) -> None: ...
def glShaderSource(shader, count, string, length) -> None: ...
def glStencilFunc(func, ref, mask) -> None: ...
def glStencilFuncSeparate(face, func, ref, mask) -> None: ...
def glStencilMask(mask) -> None: ...
def glStencilMaskSeparate(face, mask) -> None: ...
def glStencilOp(fail, zfail, zpass) -> None: ...
def glStencilOpSeparate(face, sfail, dpfail, dppass) -> None: ...
def glTexImage2D(target, level, internalformat, width, height, border, format, type, pixels) -> None: ...
def glTexImage3D(target, level, internalformat, width, height, depth, border, format, type, pixels) -> None: ...
def glTexParameterf(target, pname, param) -> None: ...
def glTexParameterfv(target, pname, params) -> None: ...
def glTexParameteri(target, pname, param) -> None: ...
def glTexParameteriv(target, pname, params) -> None: ...
def glTexSubImage2D(target, level, xoffset, yoffset, width, height, format, type, pixels) -> None: ...
def glTexSubImage3D(target, level, xoffset, yoffset, zoffset, width, height, depth, format, type, pixels) -> None: ...
def glTransformFeedbackVaryings(program, count, varyings, bufferMode) -> None: ...
def glUniform1f(location, v0) -> None: ...
def glUniform1fv(location, count, value) -> None: ...
def glUniform1i(location, v0) -> None: ...
def glUniform1iv(location, count, value) -> None: ...
def glUniform1ui(location, v0) -> None: ...
def glUniform1uiv(location, count, value) -> None: ...
def glUniform2f(location, v0, v1) -> None: ...
def glUniform2fv(location, count, value) -> None: ...
def glUniform2i(location, v0, v1) -> None: ...
def glUniform2iv(location, count, value) -> None: ...
def glUniform2ui(location, v0, v1) -> None: ...
def glUniform2uiv(location, count, value) -> None: ...
def glUniform3f(location, v0, v1, v2) -> None: ...
def glUniform3fv(location, count, value) -> None: ...
def glUniform3i(location, v0, v1, v2) -> None: ...
def glUniform3iv(location, count, value) -> None: ...
def glUniform3ui(location, v0, v1, v2) -> None: ...
def glUniform3uiv(location, count, value) -> None: ...
def glUniform4f(location, v0, v1, v2, v3) -> None: ...
def glUniform4fv(location, count, value) -> None: ...
def glUniform4i(location, v0, v1, v2, v3) -> None: ...
def glUniform4iv(location, count, value) -> None: ...
def glUniform4ui(location, v0, v1, v2, v3) -> None: ...
def glUniform4uiv(location, count, value) -> None: ...
def glUniformMatrix2fv(location, count, transpose, value) -> None: ...
def glUniformMatrix2x3fv(location, count, transpose, value) -> None: ...
def glUniformMatrix2x4fv(location, count, transpose, value) -> None: ...
def glUniformMatrix3fv(location, count, transpose, value) -> None: ...
def glUniformMatrix3x2fv(location, count, transpose, value) -> None: ...
def glUniformMatrix3x4fv(location, count, transpose, value) -> None: ...
def glUniformMatrix4fv(location, count, transpose, value) -> None: ...
def glUniformMatrix4x2fv(location, count, transpose, value) -> None: ...
def glUniformMatrix4x3fv(location, count, transpose, value) -> None: ...
def glUnmapBuffer(target) -> None: ...
def glUseProgram(program) -> None: ...
def glValidateProgram(program) -> None: ...
def glVertexAttrib1f(index, x) -> None: ...
def glVertexAttrib1fv(index, v) -> None: ...
def glVertexAttrib2f(index, x, y) -> None: ...
def glVertexAttrib2fv(index, v) -> None: ...
def glVertexAttrib3f(index, x, y, z) -> None: ...
def glVertexAttrib3fv(index, v) -> None: ...
def glVertexAttrib4f(index, x, y, z, w) -> None: ...
def glVertexAttrib4fv(index, v) -> None: ...
def glVertexAttribI4i(index, x, y, z, w) -> None: ...
def glVertexAttribI4iv(index, v) -> None: ...
def glVertexAttribI4ui(index, x, y, z, w) -> None: ...
def glVertexAttribI4uiv(index, v) -> None: ...
def glVertexAttribIPointer(index, size, type, stride, pointer) -> None: ...
def glVertexAttribPointer(index, size, type, normalized, stride, pointer) -> None: ...
def glViewport(x, y, width, height) -> None: ...

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
