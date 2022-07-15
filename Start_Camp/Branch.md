# Branch

**Head** : 추가한 새 Branch에 Head를 지정하여 수정한다

**Branch** : 기본 Master이고 추가하여(ex. feature-a, feature-b 등) 기존 상용버전을 수정한다

---

## merge
1. **fast - forward**
    기존 상용버전의 Branch에서 수정한 버전을 빨리감기 하듯이 적용하는 방법
2. **3 - way merging**
   하나의 상용버전 c1에서 feature -a 와 feature - b에 의해 브랜치가 두갈래로 나뉘었을 때 두 수정사항에 대한 master 상용버전을 찾아 해당 버전에 a1, b1 commmit을 모두 반영한 하나의 새 d1을 만들어냄 -> 새 상용버전이 됨