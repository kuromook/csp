_csp_pasteText(x, y, txt)
{
clipboard:=txt
MouseMove,x,y,30
click
sleep, 500
send,^{v}
send,+{return}
return
}

CountSubstring(fullstring, substring){
   StringReplace, junk, fullstring, %substring%, , UseErrorLevel
   return errorlevel
}

setSpeaking(scenario, backup)
{
	;msgbox, % scenario
    page := StrSplit(scenario, "`nl`n")
    startLocationX := 800+400
    startLocationY := 180

    x :=startLocationX
    y := startLocationY
    height := 180+100
    width := 10
    lineSpace := 30 + 50
    
	for index, line in page
	{      

		speak := StrSplit(line, "`n`n`n")	
		for i, txt in speak
		{
            num:=CountSubstring(txt, "`r`n")

        	_csp_pasteText(x,y, txt)
        	x:= x-lineSpace*(num+1)

		}
        
        if y < 500
        {
            y:= y+height
            x:=startLocationX
        }
    }
    _csp_pasteText(x,y,backup)
}




csp_speaking_convert(){
run, speakingConvert.exe ; your executable path
Return
}

csp_set_speaking(){
backup:=Clipboard
csp_speaking_convert()
sleep,2000
send,{t}
setSpeaking(clipboard, backup)
Return
}

#F1::  ; set shortcut as you wish
csp_set_speaking()
return