import json
import os


def PathToUser():
    return {
        "api": "PathToUser",
        "args": ""
    }

def PathToObject(object_index):
    return {
        "api": "PathToObject",
        "args": str(object_index)
    }
    
def ObjectInView(object_index):
    return {
        "api": "ObjectInView",
        "args": str(object_index)
    }
    
def SaveTopDownView(photo_path):
    return {
        "api": "SaveTopDownView",
        "args": os.path.abspath(photo_path)
    }
    
def TakePhoto(photo_path, position, rotation, width=4096, height=4096, vertical_field_of_view=90):
    return {
        "api": "TakePhoto",
        "args": json.dumps({
            "position": position,
            "rotation": rotation,
            "width": width,
            "height": height,
            "vertical_field_of_view": vertical_field_of_view,
            "path": os.path.abspath(photo_path),
            "rendering_type": ""
        })
    }
    
def TakePhotoWithVisiblityInfo(photo_path, position, rotation, width=4096, height=4096, vertical_field_of_view=90, rendering_type=""):
    return {
        "api": "TakePhotoWithVisiblityInfo",
        "args": json.dumps({
            "position": position,
            "rotation": rotation,
            "width": width,
            "height": height,
            "vertical_field_of_view": vertical_field_of_view,
            "path": os.path.abspath(photo_path),
            "rendering_type": rendering_type
        })
    }
    
def SetVideoRecordingPath(video_path):
    return {
        "api": "SetVideoRecordingPath",
        "args": os.path.abspath(video_path)
    }
    
def GetSpatialRelations():
    return {
        "api": "GetSpatialRelations",
        "args": ""
    }
    
def SaveSceneToGltf(file_path):
    return {
        "api": "SaveSceneToGltf",
        "args": os.path.abspath(file_path)
    }
    
def HideObject(object_id):
    return {
        "api": "HideObject",
        "args": str(object_id)
    }
    
def ShowObject(object_id):
    return {
        "api": "ShowObject",
        "args": str(object_id)
    }

def MoveObject(object_id, position, rotation):
    return {
        "api": "MoveObject",
        "args": json.dumps({
            "object_id": object_id,
            "position": position,
            "rotation": rotation
        })
    }

def AgentTargetObjectID():
    return {
        "api": "AgentTargetObjectID",
        "args": ""
    }

def PlayerTargetObjectID():
    return {
        "api": "PlayerTargetObjectID",
        "args": ""
    }