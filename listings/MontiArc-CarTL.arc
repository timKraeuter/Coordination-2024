component CarTL {
  port <<sync>> in Signal signal;

  automaton {
      initial state Green;
      state Red;

      Red -> Green [signal == Signal.GREEN];
      Green -> Red [signal == Signal.RED];
    }
}