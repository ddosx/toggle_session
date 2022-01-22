import libs

libs.createtmppath()
status = libs.checktempfile()
status = libs.returnstatus(status)
status = libs.toggletempfile(status)
status = libs.togglescreen(status)
