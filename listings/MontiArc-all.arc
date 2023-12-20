component PedestrianCrossing {
  CarTL ctl;
  PedestrianTL ptl;

  ctl.signal -> ptl.signal;
}

component CarTL {
  port
    <<sync>> in Signal signal;

  automaton {
      initial state Green;
      state Red;

      Red -> Green [signal == Signal.GREEN];
      Green -> Red [signal == Signal.RED];
    }
}

component PedestrianTL {
  port
    <<sync>> out Signal signal;

  automaton {
    initial state Red;
    state RedAmber;
    state Green;
    state Amber;

    Red -> RedAmber;
    RedAmber -> Green / {
      signal = Signal.RED;
    };
    Green -> Amber;
    Amber -> Red / {
      signal = Signal.GREEN;
    };
  }
}