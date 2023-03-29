// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Acme
{
    [AcmeResourceType("acme:index/registration:Registration")]
    public partial class Registration : global::Pulumi.CustomResource
    {
        [Output("accountKeyPem")]
        public Output<string> AccountKeyPem { get; private set; } = null!;

        [Output("emailAddress")]
        public Output<string> EmailAddress { get; private set; } = null!;

        [Output("externalAccountBinding")]
        public Output<Outputs.RegistrationExternalAccountBinding?> ExternalAccountBinding { get; private set; } = null!;

        [Output("registrationUrl")]
        public Output<string> RegistrationUrl { get; private set; } = null!;


        /// <summary>
        /// Create a Registration resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Registration(string name, RegistrationArgs args, CustomResourceOptions? options = null)
            : base("acme:index/registration:Registration", name, args ?? new RegistrationArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Registration(string name, Input<string> id, RegistrationState? state = null, CustomResourceOptions? options = null)
            : base("acme:index/registration:Registration", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Registration resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Registration Get(string name, Input<string> id, RegistrationState? state = null, CustomResourceOptions? options = null)
        {
            return new Registration(name, id, state, options);
        }
    }

    public sealed class RegistrationArgs : global::Pulumi.ResourceArgs
    {
        [Input("accountKeyPem", required: true)]
        public Input<string> AccountKeyPem { get; set; } = null!;

        [Input("emailAddress", required: true)]
        public Input<string> EmailAddress { get; set; } = null!;

        [Input("externalAccountBinding")]
        public Input<Inputs.RegistrationExternalAccountBindingArgs>? ExternalAccountBinding { get; set; }

        public RegistrationArgs()
        {
        }
        public static new RegistrationArgs Empty => new RegistrationArgs();
    }

    public sealed class RegistrationState : global::Pulumi.ResourceArgs
    {
        [Input("accountKeyPem")]
        public Input<string>? AccountKeyPem { get; set; }

        [Input("emailAddress")]
        public Input<string>? EmailAddress { get; set; }

        [Input("externalAccountBinding")]
        public Input<Inputs.RegistrationExternalAccountBindingGetArgs>? ExternalAccountBinding { get; set; }

        [Input("registrationUrl")]
        public Input<string>? RegistrationUrl { get; set; }

        public RegistrationState()
        {
        }
        public static new RegistrationState Empty => new RegistrationState();
    }
}
