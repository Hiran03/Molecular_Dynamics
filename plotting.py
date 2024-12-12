import pandas as pd
import matplotlib.pyplot as plt


df = pd.DataFrame(pd.read_csv(r"Tension_data.txt", sep='[\s]{2,}', header = 0, engine = 'python'))
#df = df.iloc[2:25,:]
df = df[df['Pzz']<-224]
print (df)

print(df.shape)
df["Pzz"] = -1*df["Pzz"]
df["Pzz"] = df["Pzz"] - 224
initial = df["Lz"][2]
df["Strain"] = (df["Lz"] - initial)/initial
df["Stress"] =  df["Pzz"]
X = pd.DataFrame(df["Strain"])
X["Ones"] = 1
print(X)
print(df["Stress"])
y = df["Stress"]



df["num"] = df["Stress"]*df["Strain"]
df["denom"] = df["Strain"]*df["Strain"]
m = (sum(df["num"])/ sum(df["denom"]))

plt.plot(df["Strain"], y,'ro',markersize = 3, label = "Simulation")
#plt.plot(df["Strain"], m*df["Strain"] , linewidth = 0.5, label = "Linear fit")
plt.title("Tensile Test")
plt.xlabel("Strain")
plt.ylabel("Stress (Mpa)")
plt.legend()
plt.show()

