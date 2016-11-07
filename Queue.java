package queue;

public class Queue {
	int capacity,front,rear,size;
	int[] array;
	
	public Queue(int capacity) {
		this.capacity = capacity;
		this.front=this.size=0;
		this.rear = capacity-1;
		this.array = new int[capacity];
	}
	public boolean isFull(){
		return this.size==this.capacity;
	}
	public boolean isEmpty(){
		return this.size==0;
	}
	public void enqueue(int item){
		if(this.isFull()){
			return;
		}
		this.rear = (this.rear+1)%this.capacity;
		this.array[this.rear]= item;
		this.size++;
		System.out.println("Successfully added");
	}
	public int deque(){
		if(this.isEmpty()){
			return Integer.MIN_VALUE;
		}
		int item = this.array[this.front];
		this.front = (this.front+1)%this.capacity;
		this.size--;
		return item;
	}
	public int front(){
		if(this.isEmpty()){
			return Integer.MIN_VALUE;
		}
		return this.array[this.front];
	}
	public int rear(){
		if(this.isFull())
			return Integer.MAX_VALUE;
		return this.array[this.rear];
	}
	public static void main(String args[]){
		Queue q = new Queue(10);
		q.enqueue(10);
		q.enqueue(20);
		q.enqueue(30);
		q.enqueue(40);
		System.out.println("dequeued from the queue :" + q.deque());
		System.out.println("front of the queue :" + q.front());
		System.out.println("rear of the queue :" + q.rear());
	}
	
	
}
