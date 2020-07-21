# Report of ECCPoW difficulty

1. Ethereum에서 난이도 변경 방식
2. ECCPoW 실험
   1. Boxplot
   2. 블록 분포
   3. 블록생성시간 히스토그램
   4. 블록생성시간 확률 분포
   5. 블록생성시간 로그 확률 분포

TODO: 블록생성시간 결정해야 함

## 1. Ethereum에서 난이도 변경 방식

- Genesis 파일을 생성 할 때 기본 난이도를 결정 함
  - 난이도란 블록 생성 확률의 역수
  - 난이도가 150이고 평균 블록 생성 시간이 15초라면, 해시레이트는 10 hash/sec이 됨
    - 즉, 블록 생성 확률은 1/150이 되고, 1초당 블록 생성 시도 횟수는 10회.
  - 난이도가 150인데 블록이 30초에서 생성 되었다면 해시레이트는 5 hash/sec이 되고 난이도는 75로 변경 됨
  - 블록 생성시간이 지정된 평균 블록 생성 시간$\pm$30% 일 경우 난이도는 변경되지 않음.

## 2. ECCPoW 실험

- 난이도 0 ~ 10까지 난이도 8과 10을 제외하고 600개 이상씩 생성
  - 이전에 진행한 난이도를 고정한 실험에서 블록을 600개, 1200개 1500개 생성 했을때 평균의 차이가 5% 미만이었기 때문에 600개로 실험 함.

### 2.1 Boxplot

- **Median (Q2/50th Percentile)**: the middle value of the dataset.
  - 데이터가 넓게 퍼져있는 경우 median과 Q1 또는 Q3 사이의 거리가 멈
- **Interquartile range (IQR)** : is the distance between the upper and lower quartiles.(25th to the 75th percentile.)

<p aligh="center"><img src="https://t1.daumcdn.net/cfile/tistory/996456345C34A7D830" alt="boxplot1" style="zoom:50%;" /></p> 

[Difficulty report](https://github.com/HyoungsungKim/Report-of-ECCPOW-difficulty/blob/master/report-of-eccpow-difficulty.pdf)
