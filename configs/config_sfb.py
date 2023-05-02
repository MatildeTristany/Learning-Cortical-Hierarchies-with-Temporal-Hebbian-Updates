config = {
'alpha_di': 3.794730226756921e-06,
'alpha_fb': 0.040735025334504266,
'dt_di_fb': 0.06331511239560181,
'epsilon': 9.036280827630029e-05,
'epsilon_fb': 1.754326683551049e-10,
'k_p_fb': 0.004754531889494906,
'lr': 0.0002739255103545902,
'lr_fb': 1.2579192453097163e-08,
'lr_fb_init': 1.1541743051404933e-07,
'sigma': 0.005084218073538146,
'sigma_fb': 2.310548825716637e-05,
'sigma_output': 1.8899045274846402e-05,
'time_constant_ratio': 0.010489693398661798,
'time_constant_ratio_fb': 0.018748324276889734,
'dataset': 'mnist',
'num_train': 1000,
'num_test': 1000,
'num_val': 1000,
'no_preprocessing_mnist': False,
'no_val_set': False,
'epochs': 40,
'batch_size': 128,
'target_stepsize': 0.001,
'optimizer': 'Adam',
'optimizer_fb': 'Adam',
'momentum': 0.0,
'forward_wd': 0,
'feedback_wd': 0.1,
'train_parallel': False,
'normalize_lr': False,
'epochs_fb': 20,
'freeze_forward_weights': False,
'freeze_fb_weights': True,
'freeze_fb_weights_output': True,
'shallow_training': False,
'extra_fb_epochs': 0,
'extra_fb_minibatches': 0,
'only_train_first_layer': False,
'train_only_feedback_parameters': False,
'clip_grad_norm': 1.0,
'grad_deltav_cont': True,
'beta1': 0.9,
'beta2': 0.9,
'beta1_fb': 0.9,
'beta2_fb': 0.9,
'num_hidden': 3,
'size_hidden': 256,
'size_input': 784,
'size_output': 10,
'hidden_activation': 'sigmoid',
'output_activation': 'softmax',
'no_bias': False,
'network_type': 'DFC_single_phase',
'initialization': 'xavier_normal',
'fb_activation': 'sigmoid',
'no_cuda': False,
'random_seed': 42,
'cuda_deterministic': False,
'hpsearch': False,
'multiple_hpsearch': False,
'single_precision': False,
'evaluate': False,
'out_dir': None,
'save_lu_loss': False,
'save_LU_angle': False,
'at_steady_state': False,
'save_logs': True,
'save_BP_angle': False,
'save_GN_angle': False,
'save_GNT_angle': False,
'save_condition_gn': True,
'save_df': True,
'gn_damping': 0.0,
'log_interval': 30,
'gn_damping_hpsearch': False,
'save_nullspace_norm_ratio': False,
'save_fb_statistics_init': False,
'compute_gn_condition_init': True,
'ndi': False,
'dt_di': 0.001,
'tmax_di': 500,
'tmax_di_fb': 500,
'epsilon_di': 0.5,
'reset_K': False,
'initialization_K': 'xavier_normal',
'noise_K': 0.0,
'compare_with_ndi': False,
'learning_rule': 'nonlinear_difference',
'use_initial_activations': False,
'k_p': 2.0,
'inst_system_dynamics': False,
'noisy_dynamics': True,
'fb_learning_rule': 'normal_controller',
'inst_transmission': True,
'inst_transmission_fb': True,
'apical_time_constant': -1,
'apical_time_constant_fb': 0.1,
'efficient_controller': False,
'proactive_controller': True,
'simulate_layerwise': True,
'target_class_value': 0.9,
'inst_system_dynamics_fb': False,
'low_pass_filter_u': False,
'include_non_converged_samples': True,
'tau_f': 0.5,
'tau_noise': 0.05,
'error_as_loss_grad': True,
'sum_reduction': True,
'save_checkpoints': True,
'pretrained_net_dir': '/home/matilde_tristany/code/dfc/configs/pretraining_sfb',
}