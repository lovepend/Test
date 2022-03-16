import pandas as pd
import tensorflow as tf

파일경로 = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/lemonade.csv'
레모네이드 = pd.read_csv(파일경로)

파일경로 = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/boston.csv'
보스턴 = pd.read_csv(파일경로)

파일경로 = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/iris.csv'
아이리스 = pd.read_csv(파일경로)

print(레모네이드.shape)
print(보스턴.shape)
print(아이리스.shape)

print(레모네이드.head())

#레모네이드 판매량 예상하기

#1. 과거의 데이터 준비 

# Step1. 판다스 라이브러리를 이용하여 데이터 표 정리하기
독립 = 레모네이드[['온도']]
종속 = 레모네이드[['판매량']]
print(독립.shape, 종속.shape)

# Step2. 모델의 구조를 만들기
# 가장 간단 형태로 구성 / 뉴런하나로 이루어진 두뇌를 생성
# 히든레이어는 다음시간에 ... 
X = tf.keras.layers.Input(shape=[1]) #독립변수의 개수 "온도"
Y = tf.keras.layers.Dense(1)(X) #종속변수의 개수 "판매량"

model = tf.keras.models.Model(X, Y)
model.compile(loss='mse')

#데이터로 모델을 학습하기
#epochs 는 학습 반복 횟수 의미
#verbose 는 콘솔에 출력할 정보 의미 

#model.fit(독립, 종속, epochs=1000, verbose=0)
model.fit(독립, 종속, epochs=1700)

#모델의 학습이 끝난 후 결과를 출력하기

print(model.predict(독립))
#print(model.predict([[20]]))
