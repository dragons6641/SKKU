<프로그램 개요>

원격 드론 컨트롤러로 드론을 조종하는 서버-클라이언트 기반 프로그램입니다.
명령어를 입력할 때 원하는 명령어를 입력하고 Enter키를 누르면 명령이 실행됩니다.


<프로그램 사용법>

1. <MyController.py>, <MyDrone.py> 프로그램을 각자 다른 IDLE 창에서 실행합니다.

(1-1). <MyController.py>의 command 입력 창에서 connect를 입력하면 드론과 연결이 됩니다.
이외의 커맨드를 입력 시 드론과 연결되지 않습니다.

(1-2). <MyDrone.py>은 드론의 초기 위치인 [0, 0]을 출력합니다.
이후에는 컨트롤러의 연결을 기다립니다.


2. 드론과 연결이 되면 세 가지 종류의 명령어를 입력할 수 있습니다.
이외의 커맨드를 입력 시 명령어가 드론에 전송되지 않습니다.

(2-1) w, a, s, d 중 하나를 입력하면 드론이 각각 위, 왼쪽, 아래, 오른쪽으로 움직입니다.
이동한 좌표를 드론으로부터 전송받아 화면에 출력합니다.
초기 위치는 [0, 0]이고, 이동 범위는 [0 <= X <= 9, 0 <= Y <= 9] 입니다.
10 * 10 크기의 지도를 벗어나는 명령을 입력 시, 드론은 이동하지 않습니다.

(2-2) reset을 입력하면 드론이 초기 위치인 [0, 0]으로 돌아갑니다.

(2-3) disconnect를 입력하면 드론과 연결이 끊어집니다.
이후 connect를 입력하면 드론과 다시 연결할 수 있습니다.
이 때 드론의 위치는 초기 위치인 [0, 0]이 아닌 마지막으로 이동한 위치입니다.


<포함된 기능>

숫자/문자형 자료형 변수와 이들 사이의 연산, 선택문, 반복문, 함수 등의 필수 포함 기능이 모두 들어있습니다.
응용 기능으로는 서버-클라이언트 소켓 프로그래밍을 사용했습니다.
