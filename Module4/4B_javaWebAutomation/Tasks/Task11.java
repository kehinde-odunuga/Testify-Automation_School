package Tasks;

import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

import java.util.Set;

import static org.openqa.selenium.By.className;

public class Task11 {
    public static void main(String[] args) throws InterruptedException {
        System.setProperty("webdriver.chrome.driver", "C:\\Users\\odunuga\\kehinde-testify\\SeleniumWeb\\src\\chromedriver.exe");

        //Launch browser
        WebDriver driver = new ChromeDriver();

        //Maximize the browser
        driver.manage().window().maximize();

        //Navigate to the url
        driver.get("https://www.google.com/");
        driver.findElement(By.name("q")).sendKeys("testify ltd");
        Thread.sleep(2000);
        driver.findElement(By.cssSelector("img[alt=Google]")).click();
        Thread.sleep(2000);
        driver.findElement(By.xpath("//body[1]/div[1]/div[3]/form[1]/div[1]/div[1]/div[4]/center[1]/input[1]")).click();
        Thread.sleep(2000);

        //driver.findElement(By.xpath("//*[@id=\"kp-wp-tab-overview\"]/div[1]/div/div/div/div/div/div[1]/div/div/span/a/h3")).click();
        driver.findElement(By.tagName("h3")).click();
        Thread.sleep(5000);

        JavascriptExecutor js = (JavascriptExecutor) driver;
        js.executeScript("window.scrollBy(0,document.body.scrollHeight)");
        Thread.sleep(2000);

        //Click on linkedin icon
        driver.findElement(By.xpath("//body/div[@id='__next']/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/a[1]")).click();

        Set<String> windows = driver.getWindowHandles();
        for (String window: windows) {
            driver.switchTo().window(window);
            Thread.sleep(3000);
            System.out.println(driver.getCurrentUrl());
    }

        Thread.sleep(3000);

        WebElement modalClose = driver.findElement(By.xpath("/html/body/div[4]/div/div/section/button/icon"));
        modalClose.click();

        String text = driver.findElement(By.xpath("//*[@id=\"main-content\"]/section[1]/section/div/div[2]/div[1]/h4/span")).getText();
        System.out.println(text);

        Thread.sleep(3000);

        driver.quit();
    }
}
