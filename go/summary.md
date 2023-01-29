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

### 構造体

```go
// 型名及びフィールド名は小文字にするとprivate扱いになる
type Person struct {
  FirstName string
  LastName  string
}

func main() {
  p := Person{
    FirstName: "John",
    LastName: "Doe"
  }
}
```

### マップ

```go
// map[key_type]value_type
var colors = map[string]bool{}

// 追加
colors["red"] = true

// 削除
delete(colors, "red")
```

### インターフェース

```go
type Dog struct {}
type Cat struct {}

func (d Dog) name() string {
  return "Dog"
}

func (c Cat) name() string {
  return "Cat"
}

// Goでは、関数名が同じで、引数が異なる型であっても
// エラーとなる
// これを回避できる方法としてインターフェースがある
// func printName(d Dog) {
//   fmt.Println(d.name())
// }

// func printName(c Cat) {
//   fmt.Println(c.name())
// }

// Animalという名前のインターフェースを定義し、
// name()という文字列を返す関数があることを定義
// Goではimplementsのように明示的に実装を書くのではなく、
// 関数名と引数と戻り値が全て同じレシーバーが定義されてる時、
// インターフェースが実装されていると判断される
type Animal interface {
  name() string
}

// 引数にはAnimalを型としている
// Animalインターフェースを型とすることで、
// Animalインターフェースに定義されているものを実装していれば、
// 実行できるようになる
func printName(a Animal) {
  fmt.Println(a.name())
}

func main() {
  dog := Dog{}
  cat := Cat{}
  printName(dog) // Dog
  printName(cat) // Cat
}
```

下記のメソッド(io.Copy)のドキュメントではインターフェースが用いられている実装となっている。

`dst`は`Writer`インターフェースを実装している必要があり、
`src`は`Reader`インターフェースを実装している必要がある。
`Writer`インターフェースは`Write`関数があり、`dst`はこれを実装している必要があり、
`Reader`インターフェースは`Read`関数があり、`src`はこれを実装している必要がある。

```go
func Copy(dst Writer, src Reader) (written int64, err error)

type Writer interface {
 Write(p []byte) (n int, err error)
}

type Reader interface {
 Read(p []byte) (n int, err error)
}
```

### Goルーチン

以下のようなコードだと、各サイトにアクセスしては結果を待って、次のリンクにアクセスするように実行される。これを**並行**処理(複数のことを同時にではなく、瞬間的に切り替えながら処理)するためには、Goルーチンを用いる。

また、Goルーチンは一つのコアで処理される場合は並行処理で処理されており、マルチコアである場合は並列処理で実行される。

**並行**処理は同時に実行はされず、瞬間的に切り替えながら実行されていることで、**並列**処理では同時に実行されていること。

```go
func main() {
  links := []string{
    "https://google.com",
    "https://amazon.com",
  }
  for _, link := range links {
    checkLink(link)
  }
}

func checkLink(link string) {
  _, err := http.Get(link)
  if err != nil {
    fmt.Println(link, "is down.")
    return
  }

  fmt.Println(link, "is up.")
}
```

Goルーチンを用いる場合

まず初めに、プログラム実行時にメインルーチンが作られており、`go`キーワードを使うことで、子ルーチンが作成されていく。
子ルーチンの管理はGoスケジュラーがやっており、作られた子ルーチンがブロッキング処理(http.Getのような)になったとき、メインルーチンに戻り、処理を続ける。
その際、子ルーチンが実行しきれてないことを防ぐために、`Channel`を使うことで子ルーチンが完了していることを管理できる。

```go
func main() {
 links := []string{
  "https://google.com",
  "https://amazon.com",
 }

 // stringのチャンネルを作成
 c := make(chan string)

 for _, link := range links {
  // 子ルーチンを作成
  // 子ルーチン作成対象の関数にチャンネルを渡す
  go checkLink(link, c)
 }

 for i := 0; i < len(links); i++ {
  // チャンネルに値が渡されたタイミングで実行される
  fmt.Println(<-c)
 }
}

func checkLink(link string, c chan string) {
 _, err := http.Get(link)
 if err != nil {
  // チャンネルに値を渡す
  c <- link + " is down"
  return
 }

 c <- link + " is up"
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
