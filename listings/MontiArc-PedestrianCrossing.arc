component PedestrianCrossing {
  // Define subcomponents
  CarTL ctl;
  PedestrianTL ptl;

  // Define port bindings
  ctl.signal -> ptl.signal;
}