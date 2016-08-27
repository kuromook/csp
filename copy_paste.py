#!/usr/bin/python
# encoding: utf-8
"""copy_paste: a module with two function, pbcopy and pbpaste. 
Relies on AppKit and Foundation frameworks from PyObjC."""

#On my computer, these are in 
#/System/Library/Frameworks/Python.framework
#/Versions/Current/Extras/lib/python/PyObjC
import Foundation, AppKit

def pbcopy(s):
    "Copy string argument to clipboard"
    newStr = Foundation.NSString.stringWithString_(s).nsstring()
    newData = newStr.dataUsingEncoding_(Foundation.NSUTF8StringEncoding)
    board = AppKit.NSPasteboard.generalPasteboard()
    board.declareTypes_owner_([AppKit.NSStringPboardType], None)
    board.setData_forType_(newData, AppKit.NSStringPboardType)

def pbpaste():
    "Returns contents of clipboard"
    board = AppKit.NSPasteboard.generalPasteboard()
    content = board.stringForType_(AppKit.NSStringPboardType)
    return content
