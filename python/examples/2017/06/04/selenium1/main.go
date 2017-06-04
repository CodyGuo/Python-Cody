// Run some code on play.golang.org and display the result
package main

import (
	"fmt"
	"log"

	"github.com/tebeka/selenium"
)

// java -jar selenium-server-standalone-3.4.0.jar

func main() {
	// FireFox driver without specific version chrome
	// *** Add gecko driver here if necessary (see notes above.) ***
	caps := selenium.Capabilities{"browserName": "firefox"}
	wd, err := selenium.NewRemote(caps, "")
	if err != nil {
		panic(err)
	}
	// defer wd.Quit()

	// Get simple playground interface
	wd.Get("http://www.xttblog.com/")

	articles, err := wd.FindElements(selenium.ByClassName, "excerpt-nothumbnail")
	if err != nil {
		log.Fatal(err)
	}
	log.Println("已获取完列表...")
	for _, art := range articles {
		lists, _ := art.FindElement(selenium.ByTagName, "h2")
		list, _ := lists.FindElement(selenium.ByTagName, "a")
		title, _ := list.GetAttribute("title")
		href, _ := list.GetAttribute("href")
		fmt.Printf("title --> {%v}\n", title)
		fmt.Println("href --> ", href)
	}

	// Click the run button

	// Get the result
	// div, _ := wd.FindElement(selenium.ByCSSSelector, "#output")

	// output := ""
	// // Wait for run to finish
	// for {
	// 	output, _ = div.Text()
	// 	if output != "Waiting for remote server..." {
	// 		break
	// 	}
	// 	time.Sleep(time.Millisecond * 100)
	// }

	// fmt.Printf("Got: %s\n", output)
}
