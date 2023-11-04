# nosql-from-scratch

[Link](https://youtu.be/i_vmkaR1x-I?feature=shared)

### Step 1
 get, set 메서드 구현
 index key, #line
 append only log file

### Step 2
 update가 많을 수록 필요없는 데이터가 disk에 차지하는 용량이 너무 많음
 Segment + Compaction : database 파일(log 파일)이 일정 사이즈가 되면 새로운 파일을 만듦
 Active한 파일 빼고 immutable. 
 ![segments and compaction](images/SegmentsCompaction.png)
 ![segments](images/SegmentsFiles.png)

### Step 3
 존재 하는 모든 key(index)가 memory에 들어갈 수 있어야 함. range 쿼리가 힘듬(full scan 필요)
 LST Tree, SSTable. Segment 파일에 key를 sorting하여 저장. Sparse Index


### Step 4
 그럼 데이터를 끝에만 추가하는 것이 불가능하지 않을까?
 새로운 key/value 추가시 SSTable에 바로 넣는게 아니라 memory에 존재하는 binary tree에 추가
 이 tree가 일정 사이즈를 넘어가면 SSTable로 append-only로 옮긴다(이미 순서대로 존재하기에 빠르게 수행 가능)
 ![memtable](images/Memtable.png)

### Step 5
 SSTable에 쓰기 전에 DB Crash한다면? Memtable에 있는 정보가 날아갈 수 있음
 Memtable뿐만 아니라 disk log file에도 업데이트(sort X, 맨 끝에 append-only)
 이 log 파일은 memtable flush 후에 지운다.
 ![LSM Tree](images/LSMTreeArchitecture.png)


### 데이터 읽는 순서
Read 요청 -> (1) Memtable 확인. (2) 가장 최신 SSTable부터 확인

 ![Summary](images/LSMTreeSummary.png)
