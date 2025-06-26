# ======= GLOBAL PARAMETERS =======
EXPERIMENT_NAME = 'iwr6843_single'
RADAR_FPS = 20
CAMERA_FPS = 30
MANSAVE_ENABLE = True
MANSAVE_PERIOD = 60
AUTOSAVE_ENABLE = False
AUTOSAVE_PERIOD = 600

# ======= SINGLE RADAR CONFIGURATION =======
RADAR_CFG_LIST = [
    {
        'name'            : 'IWR6843_Main',
        'cfg_port_name'   : 'COM5',
        'data_port_name'  : 'COM4',
        'cfg_file_name'   : './cfg/IWR6843_profile.cfg',
        'xlim'            : None,
        'ylim'            : (0.25, 4),
        'zlim'            : None,
        'pos_offset'      : (0, 0, 1),
        'facing_angle'    : {'angle': (0, 0, 0), 'sequence': None},
        'ES_threshold'    : {'range': (0, None), 'speed_none_0_exception': False},
    },
]

# ======= PROCESSING CONFIGS =======
FRAME_EARLY_PROCESSOR_CFG = {
    'FEP_frame_deque_length': 10,
}

VISUALIZER_CFG = {
    'dimension'               : '3D',
    'VIS_xlim'                : (-2, 2),
    'VIS_ylim'                : (0, 4),
    'VIS_zlim'                : (0, 2),
    'auto_inactive_skip_frame': int(1 * RADAR_FPS),
}

FRAME_POST_PROCESSOR_CFG = {
    'FPP_global_xlim' : (-1, 1),
    'FPP_global_ylim' : (0, 2.5),
    'FPP_global_zlim' : (-0.5, 2),
    'FPP_ES_threshold': {'range': None, 'speed_none_0_exception': True},
}

DBSCAN_GENERATOR_CFG = {
    'Default': {
        'DBS_eps': 0.3,
        'DBS_min_samples': 10,
        'DBS_cp_pos_xlim': None,
        'DBS_cp_pos_ylim': None,
        'DBS_cp_pos_zlim': (0, 1.8),
        'DBS_size_xlim'  : (0.2, 1),
        'DBS_size_ylim'  : (0.2, 1),
        'DBS_size_zlim'  : (0.2, 2),
        'DBS_sort'       : None,
    },
}

BGNOISE_FILTER_CFG = {
    'BGN_enable': False,
}

HUMAN_TRACKING_CFG = {
    'TRK_enable': True,
    'TRK_obj_bin_number': 2,
    'TRK_poss_clus_deque_length': 3,
    'TRK_redundant_clus_remove_cp_dis': 1,
}

HUMAN_OBJECT_CFG = {
    'obj_deque_length': 60,
    'dis_diff_threshold': {
        'threshold': 0.8,
        'dynamic_ratio': 0.2,
    },
    'size_diff_threshold': 1,
    'expect_pos': {
        'default': (None, None, 1.1),
        'standing': (None, None, 1.1),
        'sitting': (None, None, 0.7),
        'lying': (None, None, 0.5),
    },
    'expect_shape': {
        'default': (0.8, 0.8, 1.8),
        'standing': (0.7, 0.7, 1.5),
        'sitting': (0.3, 0.3, 0.6),
        'lying': (0.8, 0.8, 0.4),
    },
    'sub_possibility_proportion': (1.8, 1.8, 2, 0.5),
    'inactive_timeout': 5,
    'obj_delete_timeout': 60,
    'scene_xlim': FRAME_POST_PROCESSOR_CFG['FPP_global_xlim'],
    'scene_ylim': FRAME_POST_PROCESSOR_CFG['FPP_global_ylim'],
    'scene_zlim': FRAME_POST_PROCESSOR_CFG['FPP_global_zlim'],
    'standing_sitting_threshold': 0.9,
    'sitting_lying_threshold': 0.4,
    'get_fuzzy_pos_No': 20,
    'get_fuzzy_status_No': 40,
}

SAVE_CENTER_CFG = {
    'file_save_dir': './data/IWR6843_single/',
    'experiment_name': EXPERIMENT_NAME,
    'mansave_period': MANSAVE_PERIOD,
    'mansave_rdr_frame_max': int(MANSAVE_PERIOD * RADAR_FPS * 1.2),
    'mansave_cam_frame_max': int(MANSAVE_PERIOD * CAMERA_FPS * 1.2),
    'autosave_rdr_frame_max': int(AUTOSAVE_PERIOD * RADAR_FPS),
    'autosave_end_remove_period': HUMAN_OBJECT_CFG['obj_delete_timeout'] - HUMAN_OBJECT_CFG['inactive_timeout'],
    'autosave_cam_buffer': 3 * CAMERA_FPS,
}

CAMERA_CFG = {
    'name': 'Camera',
    'camera_index': 2,
    'capture_resolution': (1280, 720),
    'window_enable': False,
    'auto_inactive_skip_enable': True if VISUALIZER_CFG['auto_inactive_skip_frame'] > 0 else False,
}

EMAIL_ADDRESS = 'your_email@example.com'
RADAR_LOCATION = 'Lab Radar Station'
EMAIL_NOTIFIER_CFG = {
    'manual_token_path': './library/email_notifier_token/manual_token.json',
    'message_obj_detected': {
        'to': EMAIL_ADDRESS,
        'subject': f'Human detected in {RADAR_LOCATION}!',
        'text': 'Human detected! See below:',
        'image_in_text': [],
        'attachment': [],
    },
}

SYNC_MONITOR_CFG = {
    'rd_qsize_warning': 5,
    'sc_qsize_warning': 20,
}