## 4장. 서버 구축 시 알아야 할 필수 개념과 명령어
- 종료하는 방법
poweroff,shutdowm -P now, halt -p, init 0
- 재부팅
shutdown -r now, reboot, init 6
- 로그아웃
logout 또는 exit
- 가상 콘솔
Ctrl + Alt + F2 ~ F7
+ 일반 사용자일 때 프롬프트 $, root일 때 #
+ shutdown -h +5 - 5분 뒤 종료, shutdown -k +5 - 가짜 종료 메시지
런 레벨(Runlevel)
0 ~ 6
- 자동완성
tab키
정확성을 높여주기 때문에 사용 권장
- 히스토리 
history
history -c : 히스토리 지우기
