package Tasks;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.time.Duration;
import java.time.Instant;
import java.util.Set;
import java.util.concurrent.TimeUnit;

public class Task4 {
    public static void main(String[] args) throws InterruptedException {
        System.setProperty("webdriver.chrome.driver", "C:\\Users\\odunuga\\kehinde-testify\\SeleniumWeb\\src\\chromedriver.exe");
        //Launch browser
        WebDriver driver = new ChromeDriver();
        //Maximize the browser
        driver.manage().window().maximize();
        // Manage wait time
        driver.manage().timeouts().implicitlyWait(5, TimeUnit.SECONDS);

        //Navigate to the url
        driver.get("http://demo.guru99.com/");
        Thread.sleep(2000);

        //Click on Security project menu
        WebElement securityProjectMenu = driver.findElement(By.linkText("Security Project"));
        securityProjectMenu.click();

        driver.navigate().refresh();

        driver.findElement(By.linkText("Security Project")).click();
        Thread.sleep(2000);

        // Enter email
        WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(5));
        wait.until(ExpectedConditions.presenceOfElementLocated(By.name("uid"))).sendKeys("ok@abc.com");
        // Enter password
        driver.findElement(By.name("password")).sendKeys("your_password");
        Thread.sleep(2000);

        driver.quit();
    }
}
