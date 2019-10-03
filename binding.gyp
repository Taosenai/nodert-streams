{
  'includes': [ 'common.gypi' ],
  "targets": [
    {
      "target_name": "NodeRT_Buffer_Utils",
      "sources": [ "NodeRT.Buffer.Utils.cpp",
                  "NodeRtUtils.cpp",
                  "OpaqueWrapper.cpp"],
	  "include_dirs": [
        "<!(node -e \"require('nan')\")"
      ],
      'libraries': [ '-lruntimeobject.lib'],
      'msvs_settings': {
        'VCCLCompilerTool': {
            'AdditionalUsingDirectories' : [
              '%VCToolsInstallDir%/lib/x86/store/references',
              '%WindowsSdkDir%/UnionMetadata/%WindowsSDKVersion%'
            ],
            'AdditionalOptions': [ '/ZW']
        }
      }
     }
  ]
}
