import Options
from os import unlink, symlink, popen
from os.path import exists 

srcdir = '.'
blddir = 'build'
destdir = '.'
VERSION = '0.0.1'

def set_options(opt):
  opt.tool_options("compiler_cxx")

def configure(conf):
  conf.check_tool("compiler_cxx")
  conf.check_tool("node_addon")
  #some more clever should make this wscript file more accurate
  conf.check(header_name="sqldb.h")

def build(bld):
  obj = bld.new_task_gen("cxx", "shlib", "node_addon") 
  obj.cxxflags = ["-g", "-D_FILE_OFFSET_BITS=64", "-D_LARGEFILE_SOURCE", "-Wall"]
  # This is the name of our extension.
  obj.target = "freetds"
  obj.source = "src/node_freetds.cpp"
  obj.linkflags = ["-lsybdb"]
