package main

import (
	"fmt"
	"log"
	"os"
	"strconv"
	"time"
)

var ok bool

/* 斐波那契数列
Fibonacci(40) = 102334155
计算Fibonacci用时 --> 766.5385ms
*/
func fib(n int) int {
	if n < 2 {
		return n
	}

	return fib(n-1) + fib(n-2)
}

func main() {
	go spinner(100 * time.Millisecond)
	var n = 40
	var err error
	if len(os.Args) == 2 {
		n, err = strconv.Atoi(os.Args[1])
		if err != nil {
			log.Fatal(err)
		}
	}
	start := time.Now()
	fibN := fib(n)
	ok = true
	fmt.Printf("\rFibonacci(%d) = %d\n", n, fibN)
	fmt.Printf("计算Fibonacci用时 --> %s\n", time.Since(start))
}

// 打印动态
func spinner(delay time.Duration) {
	if !ok {
		fmt.Print("正在计算中...  ")
		for {
			for _, r := range `-\|/` {
				fmt.Printf("\b%c", r)
				time.Sleep(delay)
			}
		}
	}
}
