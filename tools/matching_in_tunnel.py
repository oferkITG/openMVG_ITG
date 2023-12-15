import os
from pathlib import Path
from typing import Type, List

import cv2
import numpy as np
import torch

from tools.features.outlier_filter import FilterType
from tools.localize_images import FrameData, MatchHypothesis, match_pair, estimate_relative_pose, draw_pointclouds_using_pangolin
from tools.pangolin_viz import Viewer
from tools.vpr_scenarios import Scenario_2023_11_27T90_37_23, VprScenario
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

if __name__ == "__main__":
    viewer: Viewer() = Viewer()
    cameras: List = []
    camera_pose = np.eye(4)
    cameras.append(camera_pose)

    scenario: Type[VprScenario] = Scenario_2023_11_27T90_37_23()
    data_path: Path = scenario.data_path
    images_path: Path = data_path / 'images'
    results_path: Path = data_path / 'results' / "matching_in_tunnel"
    os.makedirs(results_path, exist_ok=True)
    start_frame: int = 4950
    frame_range: int = 100
    K: np.ndarray = np.array([[1334.572266, 0, 960.029785],
                              [.0, 1334.572266, 728.388794],
                              [.0, .0, 1.0]])
    # matching
    frame_pairs: List[FrameData] = []
    ref_frame_index = start_frame
    accumulated_pose = np.eye(4)
    list_of_absolute_poses = [accumulated_pose]
    viewer.q_camera.put(list_of_absolute_poses)
    viewer.q_pose.put(accumulated_pose)

    for frame_offset in range(frame_range):
        frame_idx: int = start_frame + frame_offset
        img: np.ndarray = cv2.imread(str(images_path / "frame{0:d}.jpg".format(frame_idx)), cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, [img.shape[1] // 2, img.shape[0] // 2])
        # neighbor_idx: int = frame_idx if frame_offset == 0 else frame_idx - 1
        match_with_ref: MatchHypothesis = MatchHypothesis(target_frame_index=frame_idx-1, frame_idx=frame_idx)
        match_pair(match_with_ref, images_path, plot_flag=False, save_flag=True, device=device, results_path=results_path, K=K, filter_type=FilterType.EPIPOLAR)
        estimate_relative_pose(match_with_ref, K=K)
        accumulated_pose = accumulated_pose @ match_with_ref.relative_pose_wrt_target_frame
        list_of_absolute_poses.append(accumulated_pose)
        viewer.q_camera.put(list_of_absolute_poses)
        viewer.q_pose.put(accumulated_pose)
        viewer.q_image.put(img)
        key = cv2.waitKey(100)

    # draw_pointclouds_using_pangolin(list_of_camera_poses=list_of_absolute_poses,
    #                                 list_of_point_clouds=[],
    #                                 model_view_params=None,
    #                                 ground_plane_axes='xz',
    #                                 point_size=10,
    #                                 label='Absolute poses wrt target')
    cv2.waitKey(0)
