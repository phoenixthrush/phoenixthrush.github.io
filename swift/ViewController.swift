//  ViewController.swift
//  nya
//
//  Created by phoenixthrush on 04.06.21.
//

import UIKit
import AVFoundation

class ViewController: UIViewController {
    var playerLayer = AVPlayerLayer()
    @IBOutlet weak var label: UILabel!
    
    override func viewDidLoad() {
        super.viewDidLoad()
    }
    
    @IBAction func play_video(_ sender: Any) {
        playVideo()
    }
    
    @IBAction func ye_or_no(_ sender: Any) {
        let array = ["ye", "nu", "maybe"]
        label.text = array.randomElement()
    }
    
    
    func playVideo() {
        let videoURL = URL(string: "https://raw.githubusercontent.com/Phoenixthrush/phoenixthrush.github.io/master/sites/video.mp4")
        let player = AVPlayer(url: videoURL!)
        let playerLayer = AVPlayerLayer(player: player)
        playerLayer.frame = self.view.bounds
        playerLayer.videoGravity = .resizeAspect
        self.view.layer.addSublayer(playerLayer)
        player.play()
    }
    
    override func viewWillTransition(to size: CGSize, with coordinator: UIViewControllerTransitionCoordinator) {
        playerLayer.frame = CGRect(x: 0, y: 0, width: size.width, height: size.height)
    }
}
