component CarTL {
  // Define ports
  port <<sync>> in Signal signal;
  // Define behavior as automaton
  automaton {
    initial state Green;
    state Red;
    // Define transitions with event triggers
    Red -> Green [signal == Signal.GREEN];
    Green -> Red [signal == Signal.RED];
  }
}