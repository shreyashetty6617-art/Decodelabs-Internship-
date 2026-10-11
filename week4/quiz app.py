questions = [
    {"q":"Capital of India?","o":["Mumbai","Delhi","Kolkata"],"a":2},
    {"q":"Python invented in?","o":["1991","1995","2000"],"a":1},
    {"q":"2+2*2=?","o":["6","8","4"],"a":1},
]
score=0
for i,q in enumerate(questions,1):
    print(f"\nQ{i}. {q['q']}")
    for j,opt in enumerate(q['o'],1): print(f"  {j}. {opt}")
    ans=int(input("Answer 1-3: "))
    if ans==q['a']: 
        print("Correct! ✅"); score+=1
    else: print(f"Wrong! Ans is {q['a']}")
print(f"\nFinal Score: {score}/{len(questions)}")
if score==3: print("🏆 Top Performer!")
