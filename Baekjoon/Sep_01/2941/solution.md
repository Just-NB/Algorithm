## 문제

https://www.acmicpc.net/problem/2941

- 문자열 `s`가 주어지면 크로아티아 알파벳으로 변경 후 길이를 출력한다.

- 크로아티아 알파벳 8개 알파벳은 변경 후 입력해야 한다.

  | 크로아티아 알파벳 | 변경 |
  | :---------------: | :--: |
  |         č         |  c=  |
  |         ć         |  c-  |
  |        dž         | dz=  |
  |         đ         |  d-  |
  |        lj         |  lj  |
  |        nj         |  nj  |
  |         š         |  s=  |
  |         ž         |  z=  |

  

## 풀이 아이디어

### 핵심 아이디어

- 변경 후 사용가능한 알파벳은 길이 1인 알파벳과 중복되지 않는 문자로 변경한 후 길이를 출력한다

### 풀이 아이디어

- 입력된 문자열 `s`을 `replace`함수를 이용하여 변경 후 사용가능한 크로아티아 알파벳만을 변경한다.
  - ex) `c=`의 경우 `s.replace('c=','1')`