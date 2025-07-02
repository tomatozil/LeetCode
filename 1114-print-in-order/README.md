<h2><a href="https://leetcode.com/problems/print-in-order">1114. Print in Order</a></h2><h3>Easy</h3><hr><p>Suppose we have a class:</p>

<pre>
public class Foo {
  public void first() { print(&quot;first&quot;); }
  public void second() { print(&quot;second&quot;); }
  public void third() { print(&quot;third&quot;); }
}
</pre>

<p>The same instance of <code>Foo</code> will be passed to three different threads. Thread A will call <code>first()</code>, thread B will call <code>second()</code>, and thread C will call <code>third()</code>. Design a mechanism and modify the program to ensure that <code>second()</code> is executed after <code>first()</code>, and <code>third()</code> is executed after <code>second()</code>.</p>

<p><strong>Note:</strong></p>

<p>We do not know how the threads will be scheduled in the operating system, even though the numbers in the input seem to imply the ordering. The input format you see is mainly to ensure our tests&#39; comprehensiveness.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> &quot;firstsecondthird&quot;
<strong>Explanation:</strong> There are three threads being fired asynchronously. The input [1,2,3] means thread A calls first(), thread B calls second(), and thread C calls third(). &quot;firstsecondthird&quot; is the correct output.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,3,2]
<strong>Output:</strong> &quot;firstsecondthird&quot;
<strong>Explanation:</strong> The input [1,3,2] means thread A calls first(), thread B calls third(), and thread C calls second(). &quot;firstsecondthird&quot; is the correct output.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>nums</code> is a permutation of <code>[1, 2, 3]</code>.</li>
</ul>



### 풀이 방법

- 스핀 대기(while 로 폴링)   
장점: 아주 짧은 대기(≲수백 사이클)라면 OS 블록/언블록 오버헤드를 줄여줄 수 있음   
단점: 대기 시간이 조금만 길어져도 CPU를 몽땅 잡아먹고, 캐시·메모리 버스에도 부담 → 전체 수행 시간 ↑   

- 블로킹 대기(mutex+wait/notify)   
장점: CPU를 반납하고 완전 휴식 → 다른 스레드·프로세스가 CPU를 쓸 수 있음, 스케줄러 오버헤드도 줄여줌   
단점: OS 컨텍스트 스위칭 비용(수 µs~수십 µs) 발생   


