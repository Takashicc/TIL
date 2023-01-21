# Summary

### Hello World

`go run main.go`で実行。

```go
/*
実行ファイルを生成する場合は`main`にしなければならない
`main`以外だとライブラリとして利用すると判断され、
`go build`しても実行ファイルは生成されないし、
`func main`があるファイルを`go run`しても`package command-line-arguments is not a main package`
と表示されて実行されない
また、`package main`である場合、`func main`は定義しなければならない
*/
package main

import "fmt"

func main() {
    fmt.Println("Hello World")
}
```

### Go CLI

- `go build`
  - 実行ファイルを生成
- `go run`
  - その場で実行
- `go fmt`
  - ファイルをフォーマット
- `go install`
  - パッケージをコンパイルし、インストールする
- `go get`
  - パッケージのソースコードをダウンロードする
- `go test`
  - テストを実行

### 変数

```go
func main() {
  /*
  helloという名前の変数を定義。
  値から型を推測できるため、`var hello = "Hello"`
  のように省略して定義可能。
  また、`var`自体も省略可能で、`hello := "hello"`
  のように`:=`を使って定義可能。
  */
  var hello string = "Hello!"

  /*
  複数の変数を一度に定義もできる。
  値から型を推測できるため、型を省略可能。
  また、`var自体も省略可能。
  */
  var num1, num2 int = 1, 2

  /*
  以下のように定義もできる。
  */
  var (
    hello string = "Hello"
    str1, str2 = "str1", "str2"
  )
}
```

### 関数

```go
func greetings(name string) string {
  return "Hello " + name
}
```

### 配列

```go
/*
`[]`の中に要素数を入れることで、
固定サイズの配列を定義できる。
*/
var array [2]string = [2]string{"a", "b"}
```

### スライス

```go
/*
配列では`[]`に要素数を入れていたが、
何も指定しないことでスライスとして定義できる。
*/
var slice []string = []string{"a", "b"}
// slice[0:1] -> "a"
// slice[0:] -> "a", "b"
// slice[:1] -> "a"
// slice[:] -> "a", "b"

// 追加
slice = append(slice, "c")
```

### for文

```go
var numbers = []int{1, 2}

// for
for i := 0; i < len(numbers); i++ {
  fmt.Println(i, numbers[i])
}

// for ... range
for i, num := range numbers {
  fmt.Println(i, num)
}
```

### while文

while文はないため、`for`を使う。

```go
i := 0
for i < 5 {
  fmt.Println(i)
  i++
}

// 無限ループ
for {
  // do something
}
```

### メソッド

```go
type Article struct {
 author  string
 content string
}

// 通常の関数
func Create(a Article) {
  // do something
}

// メソッド
// また、通常の関数とメソッドで関数名が同じでも、
// 名前空間が異なるため、コンパイル可能
func (a Article) Create() {
 // do something
}

// メソッドには二つの定義方法があり、
// 値渡しとポインタ渡しの二通り定義できる
// 値渡しではコピーが作られ、それに対して変更を加えても元の値は影響を受けない
// ポインタ渡しにすることで、元の値を変更することができる
func (a *Article) ChangeSomething() {
  // do something
}

func main() {
 article := Article{
  author:  "著者",
  content: "内容",
 }
 article.Create()
}
```

### エラーハンドリング

```go
func main() {
  // byteSliceとerrを返却する関数
  bs, err := ioutil.ReadFile("hello.txt")
  // nilとは、初期値が設定されていない値のことで、
  // 何も保持されていない、または初期化されていないことを指す
  // つまりerr != nilとはerrに何かしら値が入っていることから
  // エラーが発生した場合の条件を意味する
  if err != nil {
    // do something when error occurs
  }
}
```

### テスト

テストを書くには、`_test.go`で終わる名前のファイルを作成し、`go test`を実行することでテストを実行できる。

```go
import "testing"

// 関数名はTestXxxの形、またはTest_xxxの形でなければならない
// Testxxxはダメ
func TestSomething(t *testing.T) {
  isError := false
  if isError {
    t.Errorf("Error!")
  }
}
```
