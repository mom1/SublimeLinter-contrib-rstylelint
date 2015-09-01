Function GetRegValue(sKey)
  On Error Resume Next
    GetRegValue = Sh.RegRead(sKey)
  If err.number Then
    GetRegValue = "ERROR:" + err.Description
    err.Clear
  End If
End Function


Dim file
Dim Path : Path = ""
Dim sArg
Dim i
i = 0
    For Each Argument In WScript.Arguments
        if i = 0 then
           sArg = Argument & Chr(34)
        else 
           sArg = sArg & " " & Argument 
        end if
        i=i+1
    Next    

Set Sh = CreateObject("WScript.Shell")
Set fso = CreateObject("Scripting.FileSystemObject")

Path = Path & GetRegValue ("HKEY_LOCAL_MACHINE\SOFTWARE\Classes\TypeLib\{ACEEF0E0-3C47-11D4-8C5D-0060080BCC06}\1.0\0\win32\")

if fso.FileExists(Path) then
  Set file = fso.GetFile(Path)
  Sh.CurrentDirectory = file.ParentFolder.Path
  Sh.Run Chr(34) & file.ParentFolder.Path & "\" & sArg ,0,1
else
  WScript.Echo "Пусто " & Path
end if