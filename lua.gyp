# Copyright (c) 2015 The Sippet Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'targets': [
    {
      'target_name': 'lua',
      'type': 'static_library',
      'include_dirs': [
        './source',
      ],
      'defines': [
        'LUA_FORWARD_IO',
      ],
      # Lua compiled as C++ do use exceptions
      'cflags_cc!': [ '-fno-exceptions' ],
      'all_dependent_settings': {
        'cflags_cc!': [ '-fno-exceptions' ],
        'include_dirs': [
          './source',
        ],
        'defines': [
          'LUA_FORWARD_IO',
        ],
      },
      'sources': [
        'source/lapi.cc',
        'source/lapi.h',
        'source/lauxlib.cc',
        'source/lauxlib.h',
        'source/lbaselib.cc',
        'source/lbitlib.cc',
        'source/lcode.cc',
        'source/lcode.h',
        'source/lcorolib.cc',
        'source/lctype.cc',
        'source/lctype.h',
        'source/ldblib.cc',
        'source/ldebug.cc',
        'source/ldebug.h',
        'source/ldo.cc',
        'source/ldo.h',
        'source/ldump.cc',
        'source/lfunc.cc',
        'source/lfunc.h',
        'source/lgc.cc',
        'source/lgc.h',
        'source/linit.cc',
        'source/liolib.cc',
        'source/llex.cc',
        'source/llex.h',
        'source/llimits.h',
        'source/lmathlib.cc',
        'source/lmem.cc',
        'source/lmem.h',
        'source/loadlib.cc',
        'source/lobject.cc',
        'source/lobject.h',
        'source/lopcodes.cc',
        'source/lopcodes.h',
        'source/loslib.cc',
        'source/lparser.cc',
        'source/lparser.h',
        'source/lprefix.h',
        'source/lstate.cc',
        'source/lstate.h',
        'source/lstring.cc',
        'source/lstring.h',
        'source/lstrlib.cc',
        'source/ltable.cc',
        'source/ltable.h',
        'source/ltablib.cc',
        'source/ltm.cc',
        'source/ltm.h',
        'source/luaconf.h',
        'source/lua.h',
        'source/lua.hpp',
        'source/lualib.h',
        'source/lundump.cc',
        'source/lundump.h',
        'source/lutf8lib.cc',
        'source/lvm.cc',
        'source/lvm.h',
        'source/lzio.cc',
        'source/lzio.h',
      ],
      'conditions': [
        ['OS=="linux"', {
            'defines': [
              'LUA_USE_LINUX',
            ],
          },
        ],
        ['OS=="mac"', {
            'defines': [
              'LUA_USE_MACOSX'
            ],
            'xcode_settings': {
              'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
              'CLANG_CXX_LANGUAGE_STANDARD': 'c++11',
              'CLANG_CXX_LIBRARY': 'libc++',  # -stdlib=libc++
            },
            'all_dependent_settings': {
              'xcode_settings': {
                'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
                'CLANG_CXX_LANGUAGE_STANDARD': 'c++11',
                'CLANG_CXX_LIBRARY': 'libc++',
              },
            },
          },
        ],
      ],
    },  # target lua
  ],
}
