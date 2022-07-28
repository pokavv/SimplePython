# SimplePython

2022.07.25 add FirstProject "printFigure"
>SourceFile: printFigure.py

2022.07.26 add SecondProject "SungJuk"
>SourceFile: Sungjukmanagement.py, openSM.py
>>@ VSCode 자체적인 문제인지 현재 input이 안먹혀서 VSCode로 실행을 못시켰다..!
    
2022.07.27 
>@ github에 commit을 해도 잔디가 안심어져서 찾아보니 제가 전에 만들었던 구글계정으로 commit해서 기록이 안된거였어요... 깃허브 사용법을 더 익혀야겠습니다 ㅋㅋㅋ

2022.07.28 add "Car_SuperCar", "reverseMsg", update "SungJuk"
>>@ 상속을 이용한 Car_SuperCar 프로그램과 역문장 출력프로그램 reverseMsg를 추가하고 SungJuk 프로그램의 오류를 수정했습니다.   
>1.Car_SuperCar : Car클래스를 부모클래스로, SuperCar클래스를 자식클래스로 하는 프로그램입니다.  
>>SourceFile: Car_SuperCar.py  
>2.reverseMsg : 문자열을 입력받으면 문자열을 거꾸로 출력하는 프로그램입니다.  
>>SourceFile: reverseMsg.py  
>3.SungJuk.py error: "TypeError: unsupported operand type(s) for /: 'builtin_function_or_method' and 'int'" 발생  
>> SungJuk.py line 19 "average = sum/4" 에서 sum이라는 'builtin_function_or_method'와 4라는 'int'가 서로 /(나누기) 연산을 할 수 가 없기때문에 발생하는 오류입니다. score_sum을 써야했는데 그냥 sum을 써서 발생한 오류입니다. 해당 줄의 'sum'을 'score_sum'으로 변경하여 오류를 해결했습니다.
