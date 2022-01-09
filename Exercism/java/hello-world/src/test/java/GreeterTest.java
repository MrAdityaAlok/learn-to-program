import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class GreeterTest {

  @Test
  public void testThatGreeterReturnsTheCorrectGreeting() {
    assertEquals("Hello, World!", new Greeter().getGreeting());
  }
}
